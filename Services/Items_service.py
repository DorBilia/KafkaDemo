from Abstract.AbstractRepo import AbstractRepo


class ItemsService:
    def __init__(self, repo: AbstractRepo):
        self.repo = repo

    def update_stock(self, order):
        item_id = order['item_id']
        item = self.repo.get_by_id(item_id)[0]
        new_quantity = item[3] - order['quantity']
        self.repo.update_column(item_id, 'stock', new_quantity)

    def get_all(self):
        return self.repo.get_all()