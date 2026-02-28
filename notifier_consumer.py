import json

from confluent_kafka import Consumer

config = {
    'bootstrap.servers': 'localhost:9092',
    "group.id": "order-notifier",
    "auto.offset.reset": "earliest"  # tells a consumer what to do if it can't find where it last left of reading
    # events, can be earliest/latest/by_duration(configured)/none(throw exception if no offset is found)
}

consumer = Consumer(config)

consumer.subscribe(['order'])
print(f"Consumer is connected to order topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        elif msg.error():
            print(f"error: {msg.error()}")
        else:
            value = msg.value().decode('utf-8')
            order = json.loads(value)
            print(f"Received order: {order['quantity']} units of {order['product']} for {order['buyer']}")
except KeyboardInterrupt:
    print("Shutting down")

finally:
    consumer.close()
