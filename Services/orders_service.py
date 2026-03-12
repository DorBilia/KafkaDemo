from Producers.orders_producer import OrderProducer
from Repositories.orders_repo import OrdersRepo


class OrdersService:
    def __init__(self):
        self.repo = OrdersRepo()
        config = {'bootstrap.servers': 'localhost:9092'}
        self.producer = OrderProducer(config)

    def make_order(self, item_id, user_id, quantity):  # TO DO: add consumer to add order to db
        order = {'item_id': item_id, 'quantity': quantity, 'user_id': user_id}
        self.producer.publish('order', order)
        self.repo.add(user_id, item_id, quantity)
