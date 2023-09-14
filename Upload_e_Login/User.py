import sqlite3

class User:
    @staticmethod
    def login(nome, password, db_path='database/users.db'):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE nome = ?', (nome,))
        user = cursor.fetchone()
        conn.close()
        if user and user[4] == password:
            return user 
        else:
            return None
