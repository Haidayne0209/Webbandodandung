from entity.category import Category


class Product:
    def __init__(self, product_id, category_id, name, price, description, url):
        self.product_id = product_id
        self.category_id = category_id
        self.name = name
        self.price = int(price) if price else 0
        self.description = description
        self.url = url
        self.cate = None

    @staticmethod
    def init_pro(id_pro, name, url, price):
        return Product(id_pro, None, name, price, '', url)

    def set_category(self, cate) -> 'Product':
        self.cate = cate if cate else Category(-1, '', '')
        return self

    @staticmethod
    def from_dict(cursor):
        product_id = cursor[0] if cursor[0] else None
        category_id = cursor[1] if cursor[1] else None
        name = cursor[2] if cursor[2] else None
        price = cursor[3] if cursor[3] else None
        description = cursor[4] if cursor[4] else None
        url = cursor[5] if cursor[5] else None

        category_name = cursor[6] if cursor[6] else '1234'
        c = Category(category_id, category_name, '')
        return Product(product_id, category_id, name, price, description, url).set_category(c)

    @staticmethod
    def from_dict_v2(obj):
        return Product(obj[5], None, obj[9], obj[10], None, obj[11])
