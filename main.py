import threading
from Consumers.notifier_consumer import Notifier
from Consumers.update_stock_consumer import StockUpdate
from Repositories.Items_repo import itemsRepo
from Services.Items_service import ItemsService
from Services.Orders_service import OrdersService
from Repositories.Users_repo import UsersRepo
from Repositories.Orders_repo import OrdersRepo
from DB.DB_handler import DBHandler
from Producers.orders_producer import OrderProducer
from Services.Users_service import UsersService


def start_consumers(consumers_to_start):
    threads = []

    for consumer in consumers_to_start:
        t = threading.Thread(target=consumer.listen, daemon=True)
        t.start()
        threads.append(t)

    return threads


def display_items(items):
    print("Nm.| Item            | Price     |In Stock")
    print("-----------------")
    for row in items:
        itemId = row['item_id']
        name = row['item_name']
        price = row['item_price']
        stock = row['item_stock']
        print(f"{itemId}. {name:<10}        : {price:<10}: {stock:<10}")


def start():
    user_id = False
    username = input("Enter your username:")
    while not user_id:
        password = input("Enter your password:")
        user_id = user_service.authenticate(username, password)
        if not user_id:
            print("Wrong password")
    while True:
        items = item_service.get_all()
        display_items(items)
        item = int(input("Enter item number: "))
        quantity = int(input("Enter quantity: "))
        item_id = items[item - 1]['item_id']
        order_service.make_order(item_id, user_id, quantity)


if __name__ == "__main__":
    db = DBHandler()

    user_repo = UsersRepo(db)
    order_repo = OrdersRepo(db)
    items_repo = itemsRepo(db)

    producer = OrderProducer({'bootstrap.servers': 'localhost:9092'})

    order_service = OrdersService(order_repo, producer)
    item_service = ItemsService(items_repo)
    user_service = UsersService(user_repo)

    config1 = {
        'bootstrap.servers': 'localhost:9092',
        "group.id": "order-notifier",
        # when multiple consumers have the same group id, only one of them gets the event
        "auto.offset.reset": "earliest"
        # tells a consumer what to do if it can't find where it last left of reading
        # events, can be earliest/latest/by_duration(configured)/none(throw exception if no offset is found)
    }

    config2 = {
        'bootstrap.servers': 'localhost:9092',
        "group.id": "order-stock",
        "auto.offset.reset": "earliest"  # tells a consumer what to do if it can't find where it last left of reading
        # events, can be earliest/latest/by_duration(configured)/none(throw exception if no offset is found)
    }

    consumers = [Notifier(config1), StockUpdate(config2, item_service)]

    start_consumers(consumers)

    start()
