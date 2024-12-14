from entity.cart_item import CartItem


class Cart:
    def __init__(self, cart_id, user_id, quantity, total):
        self.cart_id = cart_id
        self.user_id = user_id
        self.quantity = quantity
        self.total = total
        self.cart_items = []

    @staticmethod
    def from_none():
        return Cart(0, 0, 0, 0)

    def set_cart_items(self, items):
        self.cart_items = items

    @staticmethod
    def from_dict(obj):
        cart = Cart(obj[0][0], obj[0][1], obj[0][2], obj[0][3])
        cart_items = [CartItem.from_dict_v2(item) for item in obj]
        cart.set_cart_items(cart_items)
        return cart
