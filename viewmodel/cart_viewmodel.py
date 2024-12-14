from entity.cart import Cart


class CartViewModel:
    def __init__(self, cart=Cart.from_none()):
        self.cart = cart
        self.cart_items = cart.cart_items if cart.cart_items else []
        self.total = len(self.cart_items)
