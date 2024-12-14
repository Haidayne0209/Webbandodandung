from entity.product import Product


class CartItem:
    def __init__(self, cart_item_id, cart_id, product_id, quantity, price, total):
        self.cart_item_id = cart_item_id
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.total = total
        self.product = None

    def set_product(self, product):
        self.product = product

    @staticmethod
    def from_dict(obj):
        cart_item = CartItem(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
        return cart_item

    @staticmethod
    def from_dict_v2(obj):
        cart_item = CartItem(obj[4], obj[0], obj[5], obj[6], obj[7], obj[8])
        product = Product.from_dict_v2(obj)
        cart_item.set_product(product)
        return cart_item
