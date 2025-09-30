# src.model.db_manager.py

import sqlite3


class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def get_all_items(self, table_name):
        self.cursor.execute(f"""
        SELECT *
        FROM {table_name}""")
        return self.cursor.fetchall()

    def get_item(self, table_name, columns="*", where_clause=None, params=None):
        if isinstance(columns, list):
            columns = ", ".join(columns)

        query = f"""
                SELECT {columns} FROM {table_name}
                """
        if where_clause:
            query += f""" WHERE {where_clause}"""

        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def insert_item(self, table_name, data):
        """
        Inserts data into specified table
        Args:
            table_name: table name
            data (dict): column-value pairs to be inserted
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        values = tuple(data.values())

        query = f"""
                INSERT INTO {table_name}
                ({columns})
                VALUES ({placeholders})"""
        self.cursor.execute(query, values)
        self.conn.commit()
