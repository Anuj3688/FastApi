import sqlite3
import os
from handler.log_handler import log_handler


class Database:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))  # location of database.py
        self.database_name = os.path.join(base_dir, "tea_store.db")
    def create_table_tea(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TEA_HUB (
            ID TEXT,
            NAME TEXT,
            ORIGIN TEXT,
            PRICE FLOAT
            )
        ''')
        conn.commit()
        conn.close()
        return "Table Created"

    def create_table_factory(self):
        """
        factory_id,factory_name, tea_id, quantity, price
        :return:
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS FACTORY_HUB (
            factory_id TEXT,
            factory_name TEXT,
            tea_id TEXT,
            quantity INT,
            price FLOAT
            )
        ''')
        conn.commit()
        conn.close()
        return "Table Created"

    @log_handler
    def create_connection(self):
        connection = sqlite3.connect(self.database_name)
        return connection

if __name__ == '__main__':
    dep = Database()
    dep.create_table_tea()
    print(dep.create_table_tea())
    print(dep.create_table_factory())

