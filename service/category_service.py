from entity.category import Category
from service.database import MySql


def get_list_category():
    db = MySql()
    query = "SELECT * FROM category"
    result = db.select(query)
    db.close()
    return [Category.from_dict(category) for category in result]


def get_list_active_category():
    db = MySql()
    query = "SELECT * FROM category WHERE status = 'ACTIVE'"
    result = db.select(query)
    db.close()
    return [Category.from_dict(category) for category in result]


def do_add_category(name):
    db = MySql()
    query = "INSERT INTO category (name) VALUES ('{}')".format(name)
    result = db.execute(query)
    db.close()
    return result


def do_update_category(category_id, name):
    db = MySql()
    query = "UPDATE category SET name = '{}' WHERE category_id = {}".format(name, category_id)
    result = db.execute(query)
    db.close()
    return result


def get_by_id(category_id):
    db = MySql()
    query = "SELECT * FROM category WHERE category_id = {}".format(category_id)
    result = db.select(query)
    db.close()
    return Category.from_dict(result[0]) if result else None

def update_status(category_id, status):
    db = MySql()
    query = "UPDATE category SET status = '{}' WHERE category_id = {}".format(status, category_id)
    result = db.execute(query)
    db.close()
    return result