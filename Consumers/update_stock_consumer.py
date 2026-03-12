import json
from Abstract.AbstractConsumer import AbstractConsumer
from Repositories.Items_repo import itemsRepo


class StockUpdate(AbstractConsumer):
    def __init__(self, config):
        super().__init__(config, 'order')
        self.repo = itemsRepo()

    def listen(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                elif msg.error():
                    print(f"error: {msg.error()}")
                else:
                    try:
                        value = msg.value().decode('utf-8')
                        order = json.loads(value)
                        print(order)
                        self.repo.update_stock_by_order(order)
                    except KeyError:
                        print("Invalid format")

        except KeyboardInterrupt:
            print("Shutting down")
        finally:
            self.consumer.close()


config2 = {
    'bootstrap.servers': 'localhost:9092',
    "group.id": "order-stock",
    "auto.offset.reset": "earliest"  # tells a consumer what to do if it can't find where it last left of reading
    # events, can be earliest/latest/by_duration(configured)/none(throw exception if no offset is found)
}
StockUpdate(config2).listen()
