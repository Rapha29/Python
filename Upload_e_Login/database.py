import sqlite3
from flask import g

class UserDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.create_tables()  # Chame o método para criar as tabelas no construtor

    def create_tables(self):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        telefone TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")

    def get_db(self):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(self.db_path)
        return db

    def add_user(self, nome, telefone, email, password):
        query = 'INSERT INTO users (nome, telefone, email, password) VALUES (?, ?, ?, ?)'
        params = (nome, telefone, email, password)
        try:
            conn = self.get_db()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao adicionar usuário: {e}")
            return False
        
    def get_user(self, nome):
        query = 'SELECT * FROM users WHERE nome = ?'
        params = (nome,)
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                user = cursor.fetchone()
                return user
        except sqlite3.Error as e:
            print(f"Erro ao buscar usuário: {e}")
            return None

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
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                users = cursor.fetchall()
                return users
        except sqlite3.Error as e:
            print(f"Erro ao buscar todos os usuários: {e}")
            return None
    