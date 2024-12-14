from entity.order import Order
from entity.order_detail import OrderDetail
from entity.product import Product
from service.database import MySql


def get_list_order_by_user_id(user_id=None, status=None):
    db = MySql()
    query = """
                select o.order_id,
               o.user_id,
               o.total,
               o.total_quantity,
               o.address,
               o.full_name,
               o.email,
               o.phone,
               o.payment,
               o.status,
               o.created_at,
               od.product_id,
               p.name,
               p.url,
               p.price,
               od.quantity,
               od.total as od_total
        from `order` o
                 INNER join order_detail od on od.order_id = o.order_id
                 inner join product p on p.product_id = od.product_id
        where TRUE
         AND o.user_id = IF('{0}' = 'None', o.user_id, '{0}')
            AND o.status = IF('{1}' = 'None', o.status, '{1}')
        ORDER BY o.created_at DESC;
    """.format(user_id if user_id else 'None', status if status else 'None')
    result = db.select(query)
    db.close()
    orders = {}
    for row in result:
        order_id = row[0]
        if order_id not in orders:
            orders[order_id] = Order.from_dict(row)

        product_id = row[11]
        product_name = row[12]
        product_url = row[13]
        product_price = row[14]
        quantity = row[15]
        total = row[16]
        order_item = OrderDetail(quantity, total)
        pro = Product.init_pro(product_id, product_name, price=product_price, url=product_url)
        order_item.set_product(pro)
        orders[order_id].items.append(order_item)

    return list(orders.values())


def cancel_order(order_id):
    return update_order(order_id, 'CANCEL')


def update_order(order_id, status):
    db = MySql()
    query = """
        update `order` set status = '{}' where order_id = {}
    """.format(status, order_id)
    result = db.execute(query)
    db.close()
    return result
