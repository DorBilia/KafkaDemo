from Producers.orders_producer import OrderProducer
from Abstract.AbstractRepo import AbstractRepo


class OrdersService:
    def __init__(self, repo: AbstractRepo, producer):
        self.repo = repo
        self.producer = producer

    def make_order(self, item_id, user_id, quantity):
        order = {'item_id': item_id, 'quantity': quantity, 'user_id': user_id}
        self.producer.publish('order', order)
        self.repo.add(order)

