from service.database import MySql


def create_order(user_id, address, full_name, phone, email, payment_method, txn_ref=''):
    db = MySql()
    query = """
        insert into `order`(user_id, address, full_name, email, phone, payment, txn_ref) 
        VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}')
    """.format(
        user_id, address, full_name, phone, email, payment_method, txn_ref)
    result = db.execute(query)

    query_update = '''
        UPDATE `order` o
        JOIN (
            SELECT order_id, 
                   SUM(total) AS total, 
                   SUM(quantity) AS total_quantity
            FROM order_detail
            GROUP BY order_id
        ) od ON o.order_id = od.order_id
        SET o.total = od.total, 
            o.total_quantity = od.total_quantity
    '''

    db.execute(query_update)
    db.close()
    return result


def update_order_status(txn_ref, status):
    db = MySql()
    query = """
        update `order` set status = '{}' where txn_ref = '{}'
    """.format(status, txn_ref)
    result = db.execute(query)
    db.close()
    return result
