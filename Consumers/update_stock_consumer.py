import json
from Abstract.AbstractConsumer import AbstractConsumer
from Services.Items_service import ItemsService


class StockUpdate(AbstractConsumer):
    def __init__(self, config, service):
        super().__init__(config, 'order')
        self.service = service

    def handle_event(self, msg):
        try:
            value = msg.value().decode('utf-8')
            order = json.loads(value)
            self.service.update_stock(order)
        except KeyError:
            print("Invalid format")


config2 = {
    'bootstrap.servers': 'localhost:9092',
    "group.id": "order-stock",
    "auto.offset.reset": "earliest"  # tells a consumer what to do if it can't find where it last left of reading
    # events, can be earliest/latest/by_duration(configured)/none(throw exception if no offset is found)
}
StockUpdate(config2).listen()
