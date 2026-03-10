from Repositories.Items_repo import itemsRepo
from Repositories.orders_repo import OrdersRepo


# from Consumers.notifier_consumer import Notifier
# from Consumers.update_stock_consumer import StockUpdate


def display_items(items):
    index = 1
    print("Nm.| Item            | Price     |In Stock")
    print("-----------------")
    for row in items:
        itemId = row['item_id']
        name = row['item_name']
        price = row['item_price']
        stock = row['item_stock']
        print(f"{itemId}. {name:<10}        : {price:<10}: {stock:<10}")
        index += 1


class KafkaDemo:
    def __init__(self):
        self.itemRepo = itemsRepo()
        self.ordersRepo = OrdersRepo()

    def start(self):
        username = input("Enter your username:")
        while True:
            items = self.itemRepo.get_items()
            display_items(items)
            item = int(input("Enter item number: "))
            quantity = int(input("Enter quantity: "))
            item_id = items[item - 1]['item_id']
            item_name = items[item - 1]['item_name']
            self.ordersRepo.make_order(item_id, item_name, username, quantity)


if __name__ == "__main__":
    app = KafkaDemo()

    # Notifier(config1).listen()
    # StockUpdate(config2).listen()

    app.start()
