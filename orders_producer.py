import json
import uuid

from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})

order = {
    "order_id": str(uuid.uuid4()),
    "buyer": "buyer1",
    "product": "product1",
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
