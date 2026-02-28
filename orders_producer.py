import json

from confluent_kafka import Producer


def delivery_status(err, msg):
    if err:
        print(f"Error {msg}")
    else:
        print(f"Delivered! {msg.value().decode("utf-8")}\nDelivered to topic:{msg.topic()}")


class OrderProducer:
    def __init__(self):
        config = {'bootstrap.servers': 'localhost:9092'}
        self.producer = Producer(config)

    def produce_order(self, order):
        value = json.dumps(order).encode("utf-8")

        self.producer.produce(topic="order", value=value, callback=delivery_status)
        self.producer.flush()  # All buffered event are sent before exiting
