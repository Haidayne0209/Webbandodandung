class Order:
    def __init__(self, order_id, user_id, total, total_quantity, address, full_name, email, phone, payment, status,
                 created_at=None, updated_at=None):
        self.order_id = order_id
        self.user_id = user_id
        self.total = total
        self.total_quantity = total_quantity
        self.address = address
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.payment = payment
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.items = []

    @staticmethod
    def from_dict(cursor):
        order_id = cursor[0]
        user_id = cursor[1]
        total = cursor[2]
        total_quantity = cursor[3]
        address = cursor[4]
        full_name = cursor[5]
        email = cursor[6]
        phone = cursor[7]
        payment = cursor[8]
        status = cursor[9]
        created_at = cursor[10]
        return Order(order_id, user_id, total, total_quantity, address, full_name, email, phone, payment, status,
                     created_at)

    def __str__(self):
        return f"Order ID: {self.order_id}, User ID: {self.user_id}, Total: {self.total}, Total Quantity: {self.total_quantity}, Address: {self.address}, Full Name: {self.full_name}, Email: {self.email}, Phone: {self.phone}, Payment: {self.payment}, Status: {self.status}, Created At: {self.created_at}, Updated At: {self.updated_at}"