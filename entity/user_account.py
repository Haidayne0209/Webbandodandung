class UserAccount:
    def __int__(self, user_id, email, password, fullname, phone, address, role, status):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.fullname = fullname
        self.phone = phone
        self.address = address
        self.role = role
        self.status = status

    def __init__(self, cursor):
        self.user_id = cursor[0] if cursor[0] else None
        self.email = cursor[1] if cursor[1] else None
        self.password = cursor[2] if cursor[2] else None
        self.fullname = cursor[3] if cursor[3] else None
        self.phone = cursor[4] if cursor[4] else None
        self.address = cursor[5] if cursor[5] else None
        self.role = cursor[6] if cursor[6] else None
        self.status = cursor[9] if cursor[9] else None
