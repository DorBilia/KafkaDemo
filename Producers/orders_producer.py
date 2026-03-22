import json
from Abstract.AbstractProducer import AbstractProducer


def delivery_status(err, msg):
    if err:
        print(f"Error {msg}")
    else:
        print(f"Delivered! {msg.value().decode("utf-8")}\nDelivered to topic:{msg.topic()}")


class OrderProducer(AbstractProducer):

    def publish(self, topic, order):
        value = json.dumps(order).encode("utf-8")
        self.producer.produce(topic=topic, value=value, callback=delivery_status)
        self.producer.flush()  # All buffered event are sent before exiting
