import json

from confluent_kafka import Consumer
from DB_handler import DBConnection

conn = DBConnection()
print("Connected to DB")


def execute(query, params=None, fetch=False):
    cur = conn.cursor()
    cur.execute(query, params)
    if fetch:
        return cur.fetchall()
    conn.commit()
    cur.close()


def update_stock(order):
    sql = """
        UPDATE stock SET item_stock = item_stock - %s 
        WHERE item_id = %s
    """
    execute(sql, params=(order['quantity'], order['item_id']))
    print(f'Updated stock quantity of item {order['product']}')


config = {
    'bootstrap.servers': 'localhost:9092',
    "group.id": "order-stock",
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
            try:
                value = msg.value().decode('utf-8')
                order = json.loads(value)
                update_stock(order)
            except KeyError:
                print("Invalid format")

except KeyboardInterrupt:
    print("Shutting down")

finally:
    consumer.close()
