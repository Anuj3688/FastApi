import sqlite3

class Database:
    database_name = "tea_store.db"
    def create_table(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TEA_HUB (
            ID INT,
            NAME TEXT,
            ORIGIN TEXT,
            PRIZE FLOAT
            )
        ''')
        conn.commit()
        conn.close()
        return "Table Created"

    def create_connection(self):
        connection = sqlite3.connect(self.database_name)
        return connection

