from entity.cart import Cart
from service.database import MySql


def get_cart_by_user_id(user_id):
    db = MySql()
    query = """
            select c.cart_id,
               c.user_id,
               c.quantity,
               c.total,
               cd.cart_detail_id,
               cd.product_id,
               cd.quantity,
               cd.price,
               cd.total,
               p.name,
               p.price,
               p.url
        from cart c
        inner join cart_detail cd on c.cart_id = cd.cart_id
        inner join product p on cd.product_id = p.product_id
        where c.user_id = {}
    """.format(user_id)
    result = db.select(query)
    db.close()
    print(result)
    return Cart.from_dict(result) if len(result) > 0 else Cart.from_none()


def add_to_cart(user_id, product_id, quantity):
    db = MySql()
    query = "add_to_cart"
    db.call_proc(query, [user_id, product_id, quantity])
    db.close()


def remove_cart_item(cart_item_id):
    db = MySql()
    query = "remove_cart_item"
    db.call_proc(query, [cart_item_id])
    db.close()
