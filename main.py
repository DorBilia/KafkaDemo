from Manager import Manager

manager = Manager()


def display_items(items):
    index = 1
    print("Nm.| Item     | Stock")
    print("-----------------")
    for row in items:
        name = row['item_name']
        stock = row['item_stock']
        print(f"{index}. {name:<10}: {stock:<10}")
        index += 1


def start():
    username = input("Enter your username:")
    while True:
        items = manager.get_items()
        display_items(items)
        item = int(input("Enter item number: "))
        quantity = int(input("Enter quantity: "))
        id = items[item - 1]['item_id']
        name = items[item - 1]['item_name']
        manager.make_order(id, name, quantity, username)


if __name__ == "__main__":
    start()