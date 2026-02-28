import uuid

from orders_producer import OrderProducer
from DB_handler import DBHandler


class Manager:
    def __init__(self):
        self.db = DBHandler()
        self.producer = OrderProducer()

    def get_items(self):
        sql = """SELECT * FROM stock"""
        data = self.db.execute(sql, fetch=True)
        dictData = []
        for row in data:
            dictData.append({'item_id': row[2], 'item_name': row[0], 'item_stock': row[1]})
        return dictData

    def make_order(self, item_id, item_name, quantity, username):
        order = {'order_id': uuid.uuid5(), 'item_id': item_id, 'quantity': quantity, 'product': item_name,
                 'buyer': username}
        self.producer.produce_order(order)
