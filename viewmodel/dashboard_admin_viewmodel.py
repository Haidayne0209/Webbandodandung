class DashBoardAdminViewModel:
    def __init__(self, total_user, total_product, total_order, total_revenue):
        self.total_user = total_user
        self.total_product = total_product
        self.total_order = total_order
        self.total_revenue = total_revenue
        self.from_date = None
        self.to = None
        self.revenue_today = None
        self.revenue_range = None

    def set_from_to(self, from_d, to):
        self.from_date = from_d
        self.to = to

    def set_revenue(self, today_val, range_val):
        self.revenue_today = today_val
        self.revenue_range = range_val
