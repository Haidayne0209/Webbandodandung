from entity.product import Product
from service.database import MySql


def get_list_product(cate_id=-1, key=''):
    db = MySql()
    query = """
    SELECT p.product_id,
               p.category_id,
               p.name,
               p.price,
               p.description,
               p.url,
               c.name as category_name
    FROM product p
        INNER JOIN category c ON p.category_id = c.category_id AND c.status = 'ACTIVE'
    WHERE TRUE 
    AND p.status = 'ACTIVE'
    AND (p.category_id = {} OR {} = -1)
    AND (p.name LIKE '%{}%' OR '{}' = '')
    """.format(cate_id, cate_id, key, key)
    result = db.select(query)
    db.close()
    return [Product.from_dict(product) for product in result]


def get_by_id(product_id):
    db = MySql()
    query = """
    SELECT p.product_id,
               p.category_id,
               p.name,
               p.price,
               p.description,
               p.url,
               c.name as category_name
    FROM product p
        INNER JOIN category c ON p.category_id = c.category_id AND c.status = 'ACTIVE'
    WHERE TRUE 
    AND p.status = 'ACTIVE'
    AND p.product_id = {}
    """.format(product_id)
    result = db.select(query)
    db.close()
    return Product.from_dict(result[0]) if result else None


def top_9():
    db = MySql()
    query = """
        SELECT p.product_id,
               p.category_id,
               p.name,
               p.price,
               p.description,
               p.url,
               c.name as category_name
        FROM product p
                 INNER JOIN category c ON p.category_id = c.category_id AND c.status = 'ACTIVE'
        WHERE p.status = 'ACTIVE'
        ORDER BY p.created_at DESC
        LIMIT 9
    """
    result = db.select(query)
    db.close()
    return [Product.from_dict(cursor=product) for product in result]


def add_product(name, category_id, price, description, url):
    db = MySql()
    query = """
    INSERT INTO product (category_id, name, price, description, url)
    VALUES ({}, '{}', {}, '{}', '{}')
    """.format(category_id, name, price, description, url)
    db.execute(query)
    db.close()


def update_product(product_id, name, category_id, price, description, url):
    db = MySql()
    name_sql = '''
    , name = '{}'
    '''.format(name) if name != '' or name is not None else ''

    price_sql = '''
    , price = {}
    '''.format(price) if price != '' or price is not None else ''

    description_sql = '''
    , description = '{}'
    '''.format(description) if description != '' or description is not None else ''

    url_sql = '''
    , url = '{}'
    '''.format(url) if url != '' or url is not None else ''

    query = """
    UPDATE product
    SET category_id = {}
        {}
        {}
        {}
        {}
    WHERE product_id = {}
    """.format(category_id,
               name_sql,
               price_sql,
               description_sql,
               url_sql,
               product_id)

    print(query)
    db.execute(query)
    db.close()


def delete_product(product_id):
    db = MySql()
    query = """
    UPDATE product
    SET status = 'INACTIVE'
    WHERE product_id = {}
    """.format(product_id)
    db.execute(query)
    db.close()
