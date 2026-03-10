from DB.DB_handler import DBHandler


class itemsRepo():
    def __init__(self):
        self.conn = DBHandler()

    def get_items(self):
        sql = """SELECT * FROM items ORDER BY id ASC"""
        data = self.conn.execute(sql, fetch=True)
        dictData = []
        for row in data:
            dictData.append({'item_id': row[0], 'item_name': row[1], 'item_price': row[2], 'item_stock': row[3]})
        return dictData

    def update_stock_by_order(self, order):
        sql = """UPDATE items SET stock = stock - %s 
            WHERE id = %s """
        self.conn.execute(sql, params=(order['quantity'], order['item_id']))
        print(f'Updated stock quantity of item {order['product']}')
