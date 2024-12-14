from entity.user_account import UserAccount
from service.database import MySql


def login(email, password):
    db = MySql()
    query = "SELECT * FROM user_account WHERE email = '{}' AND password = '{}'".format(email, password)
    result = db.select(query)
    db.close()
    if len(result) == 0:
        return None
    return UserAccount(result[0])


def register(email, password, name):
    db = MySql()
    # check if email already exists
    query = "SELECT * FROM user_account WHERE email = '{}'".format(email)
    result = db.select(query)
    if len(result) > 0:
        return False

    query = "INSERT INTO user_account (email, password, full_name) VALUES ('{}', '{}', '{}')".format(email, password,
                                                                                                     name)
    result = db.execute(query)
    db.close()
    return result


def update_status(user_id, status):
    db = MySql()
    query = "UPDATE user_account SET status = '{}' WHERE user_id = {}".format(status, user_id)
    result = db.execute(query)
    db.close()
    return result


def lock(user_id):
    return update_status(user_id, 'INACTIVE')


def unblock(user_id):
    return update_status(user_id, 'ACTIVE')


def get_list_user():
    db = MySql()
    query = "SELECT * FROM user_account WHERE role = 'USER'"
    result = db.select(query)
    db.close()
    return [UserAccount(user) for user in result]


def get_profile(user_id):
    db = MySql()
    query = "SELECT * FROM user_account WHERE user_id = {}".format(user_id)
    result = db.select(query)
    db.close()
    return UserAccount(result[0]) if len(result) > 0 else None
