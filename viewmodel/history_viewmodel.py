class HistoryViewModel:
    def __init__(self, user, list_done, list_cancel, list_wait, list_shipping):
        self.user = user
        self.list_done = list_done
        self.list_cancel = list_cancel
        self.list_wait = list_wait
        self.list_shipping = list_shipping
