from Abstract.AbstractRepo import AbstractRepo
from psycopg2 import sql


class itemsRepo(AbstractRepo):

    def get_all(self):
        sql = """SELECT * FROM items ORDER BY id ASC"""
        data = self.conn.execute(sql, fetch=True)
        dictData = []
        for row in data:
            dictData.append({'item_id': row[0], 'item_name': row[1], 'item_price': row[2], 'item_stock': row[3]})
        return dictData

    def add(self, item):
        sql = """INSERT INTO items VALUES (%s, %s, %s)"""
        self.conn.execute(sql, (item['item_id'], item['item_name'], item['item_price'], item['item_stock']))

    def get_by_id(self, item_id):
        sql = """SELECT * FROM items WHERE id = %s"""
        return self.conn.execute(sql, (item_id,), fetch=True)

    def update_column(self, item_id, column, newValue):
        table = 'items'
        query = sql.SQL("UPDATE {table} SET {column} = %s WHERE id = %s").format(
            table=sql.Identifier(table),
            column=sql.Identifier(column)
        )
        self.conn.execute(query, (newValue, item_id))

    def delete_by_id(self, item_id):
        sql = """DELETE FROM items WHERE id = %s """
        self.conn.execute(sql, (item_id,))
