import json
from Abstract.AbstractConsumer import AbstractConsumer


class Notifier(AbstractConsumer):
    def __init__(self, config):
        super().__init__(config, 'order')

    def handle_event(self, msg):
        value = msg.value().decode('utf-8')
        order = json.loads(value)
        print(f"Received order: {order['quantity']} units of item # {order['item_id']} for user # {order['user_id']}")
