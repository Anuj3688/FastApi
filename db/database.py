import sqlite3


class Database:
    def __init__(self):
        conn = sqlite3.connect('tea_store.db')
        cursor = conn.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS TEA_HUB (
            ID TEXT,
            NAME TEXT,
            ORIGIN TEXT,
            PRIZE TEXT
            )
        ''')