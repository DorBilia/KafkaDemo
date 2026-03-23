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
            print("updated stock")
        except KeyError:
            print("Invalid format")
