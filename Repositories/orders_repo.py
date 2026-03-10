from DB.DB_handler import DBHandler
from Producers.orders_producer import OrderProducer
from Repositories.Users_repo import UsersRepo


class OrdersRepo:
    def __init__(self):
        self.conn = DBHandler()
        config = {'bootstrap.servers': 'localhost:9092'}
        self.producer = OrderProducer(config)  # to change producer placement
        self.users = UsersRepo()

    def make_order(self, item_id, item_name, username, quantity):
        sql = """INSERT INTO orders (user_id, item_id, quantity) VALUES
        (%s,%s,%s)"""
        # user_id = self.users.get_user_id_by_name(username)
        self.conn.execute(sql, params=(3, item_id, quantity))
        order = {'item_id': item_id, 'quantity': quantity, 'product': item_name,
                 'buyer': username}
        self.producer.publish('order', order)
