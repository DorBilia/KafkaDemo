from DB.DB_handler import DBHandler
from Producers.orders_producer import OrderProducer
from Repositories.Users_repo import UsersRepo


class OrdersRepo:
    def __init__(self):
        self.conn = DBHandler()
        self.users = UsersRepo()

    def add(self, user_id, item_id, quantity):
        sql = """INSERT INTO orders (user_id, item_id, quantity) VALUES
        (%s,%s,%s)"""
        self.conn.execute(sql, params=(user_id, item_id, quantity))
