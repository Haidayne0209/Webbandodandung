from service.database import MySql
from viewmodel.dashboard_admin_viewmodel import DashBoardAdminViewModel


def get_dash_board(f, t):
    db = MySql()
    query = '''
        select count(1)
        from user_account
        where role = 'user' and status = 'active';
    '''
    result = db.select(query)
    total_user = result[0][0] if result else 0

    query = '''
        select count(1)
        from product
        where status = 'active';
    '''
    result = db.select(query)
    total_products = result[0][0] if result else 0

    query = '''
            select count(1)
            from `order`;
        '''
    result = db.select(query)
    total_order = result[0][0] if result else 0

    query = '''
        select IFNULL( sum(total), 0)
        from `order`
        where status = 'done';
    '''

    result = db.select(query)
    total_revenue = result[0][0] if result else 0
    range_revenue = 0
    if f and t:
        query = '''
            select ifnull(sum(total), 0) as total
            from `order`
            where  true
                and date(created_at) >= '{}'
              and date(created_at) <= '{}'
              and status = 'done'; 
        '''.format(f, t)
        print(query)
        result = db.select(query)
        range_revenue = result[0][0] if result else 0

    query = '''
            select ifnull(sum(total), 0) as total
            from `order`
            where date(created_at) = date(now())
            and status = 'done'; 
        '''

    result = db.select(query)
    today_revenue = result[0][0] if result else 0

    model = DashBoardAdminViewModel(total_user, total_products, total_order, total_revenue)
    model.set_revenue(today_revenue, range_revenue)
    print(model)
    return model
