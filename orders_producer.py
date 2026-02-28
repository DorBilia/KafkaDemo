import json
import uuid

from confluent_kafka import Producer

config = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(config)

order = {
    "order_id": str(uuid.uuid4()),
    "buyer": "buyer1",
    "item_id": 'deb886ae-8249-42dc-a09a-2740650180d8',
    "product": "keyboard",
    "quantity": 10
}

value = json.dumps(order).encode("utf-8")


def delivery_status(err, msg):
    if err:
        print(f"Error {msg}")
    else:
        print(f"Delivered! {msg.value().decode("utf-8")}\nDelivered to topic:{msg.topic()}")


producer.produce(topic="order", value=value, callback=delivery_status)

producer.flush()  # All buffered event are sent before exiting
