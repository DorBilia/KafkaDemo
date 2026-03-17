from DB.DB_handler import DBHandler
from Repositories.Users_repo import UsersRepo
from Abstract.AbstractRepo import AbstractRepo


class OrdersRepo(AbstractRepo):
    def __init__(self):
        self.conn = DBHandler()
        self.users = UsersRepo()

    def add(self, order):
        sql = """INSERT INTO orders (user_id, item_id, quantity) VALUES
        (%s,%s,%s)"""
        self.conn.execute(sql, params=(order['user_id'], order['item_id'], order['quantity']))

    def get_all(self):
        sql = """SELECT * FROM orders"""
        return self.conn.execute(sql, fetch=True)

    def get_by_id(self, order_id):
        sql = """SELECT * FROM orders WHERE order_id = %s"""
        return self.conn.execute(sql, (order_id,), fetch=True)

    def update_column(self, order_id, column, newValue):
        sql = """UPDATE orders SET %s = %s
            WHERE id = %s """
        self.conn.execute(sql, params=(column, newValue, order_id))
    def delete_by_id(self, order_id):
        sql = """DELETE FROM orders WHERE order_id = %s """
        self.conn.execute(sql, (order_id,))
