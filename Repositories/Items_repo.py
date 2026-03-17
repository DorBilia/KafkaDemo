from DB.DB_handler import DBHandler
from Abstract.AbstractRepo import AbstractRepo


class itemsRepo(AbstractRepo):
    def __init__(self):
        self.conn = DBHandler()

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
        sql = """UPDATE items SET %s = %s
            WHERE id = %s """
        self.conn.execute(sql, params=(column, newValue, item_id))

    def delete_by_id(self, item_id):
        sql = """DELETE FROM items WHERE id = %s """
        self.conn.execute(sql, (item_id,))
