import sqlite3

class UserDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('database/users.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS uploads (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    file_path TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')

            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Erro ao executar consulta: {e}")
            return False

    def add_user(self, nome, telefone, email, password):
        query = 'INSERT INTO users (nome, telefone, email, password) VALUES (?, ?, ?, ?)'
        params = (nome, telefone, email, password)
        return self.execute_query(query, params)

    def get_user(self, nome):
        query = 'SELECT * FROM users WHERE nome = ?'
        params = (nome,)
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def update_user(self, nome, new_password):
        query = 'UPDATE users SET password = ? WHERE nome = ?'
        params = (new_password, nome)
        return self.execute_query(query, params)

    def delete_user(self, nome):
        query = 'DELETE FROM users WHERE nome = ?'
        params = (nome,)
        return self.execute_query(query, params)

    def get_all_users(self):
        query = 'SELECT * FROM users'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_upload(self, user_id, file_path):
        query = 'INSERT INTO uploads (user_id, file_path) VALUES (?, ?)'
        params = (user_id, file_path)
        return self.execute_query(query, params)

    def get_user_uploads(self, user_id):
        query = 'SELECT file_path FROM uploads WHERE user_id = ?'
        params = (user_id,)
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
