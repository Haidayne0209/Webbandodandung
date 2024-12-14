class Category:
    def __init__(self, category_id, name, status):
        self.category_id = category_id
        self.name = name
        self.status = status

    @staticmethod
    def from_dict(data):
        category_id = data[0] if data[0] in data else None
        name = data[1] if data[1] in data else None
        return Category(category_id, name, 'ACTIVE')
