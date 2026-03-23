from Abstract.AbstractRepo import AbstractRepo
from psycopg2 import sql


class OrdersRepo(AbstractRepo):

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
        table = 'orders'
        query = sql.SQL("UPDATE {table} SET {column} = %s WHERE id = %s").format(
            table=sql.Identifier(table),
            column=sql.Identifier(column)
        )
        self.conn.execute(query, (newValue, order_id))

    def delete_by_id(self, order_id):
        sql = """DELETE FROM orders WHERE order_id = %s """
        self.conn.execute(sql, (order_id,))
