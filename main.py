from Repositories.Items_repo import itemsRepo
from Services.orders_service import OrdersService
from Repositories.Users_repo import UsersRepo

def display_items(items):
    print("Nm.| Item            | Price     |In Stock")
    print("-----------------")
    for row in items:
        itemId = row['item_id']
        name = row['item_name']
        price = row['item_price']
        stock = row['item_stock']
        print(f"{itemId}. {name:<10}        : {price:<10}: {stock:<10}")


class KafkaDemo:
    def __init__(self):
        self.users = UsersRepo()
        self.itemRepo = itemsRepo()
        self.ordersService = OrdersService()

    def start(self):
        username = input("Enter your username:")
        user_id = self.users.get_user_id_by_name(username)
        while True:
            items = self.itemRepo.get_items()
            display_items(items)
            item = int(input("Enter item number: "))
            quantity = int(input("Enter quantity: "))
            item_id = items[item - 1]['item_id']
            self.ordersService.make_order(item_id, user_id, quantity)


if __name__ == "__main__":
    app = KafkaDemo()

    # Notifier(config1).listen()
    # StockUpdate(config2).listen()

    app.start()
