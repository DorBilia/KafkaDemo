import json
from Abstract.AbstractConsumer import AbstractConsumer


class Notifier(AbstractConsumer):
    def __init__(self, config):
        super().__init__(config, 'order')

    def listen(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                elif msg.error():
                    print(f"error: {msg.error()}")
                else:
                    value = msg.value().decode('utf-8')
                    order = json.loads(value)
                    print(f"Received order: {order['quantity']} units of item # {order['item_id']} for user # {order['user_id']}")
        except KeyboardInterrupt:
            print("Shutting down")

        finally:
            self.consumer.close()
config1 = {
    'bootstrap.servers': 'localhost:9092',
    "group.id": "order-notifier",
    # when multiple consumers have the same group id, only one of them gets the event
    "auto.offset.reset": "earliest"
    # tells a consumer what to do if it can't find where it last left of reading
    # events, can be earliest/latest/by_duration(configured)/none(throw exception if no offset is found)
}
Notifier(config1).listen()