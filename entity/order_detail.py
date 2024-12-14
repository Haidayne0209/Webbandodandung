class OrderDetail:
    def __init__(self, quantity, total):
        self.quantity = quantity
        self.total = total
        self.product = 0

    def set_product(self, pro):
        self.product = pro
