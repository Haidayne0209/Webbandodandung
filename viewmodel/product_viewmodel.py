class ProductViewModel:
    def __init__(self, cate1, cate2, data, cate_id, page, key):
        self.cate1 = cate1
        self.cate2 = cate2
        self.data = data
        self.cate_id = int(cate_id) if cate_id is not None else None
        self.page = page
        self.total_product = len(data)
        self.key = key
