class OutOfStockError(Exception):
    def __init__(self, item_name, requested_quantity):
        pass
        # TODO: store self.item_name and self.requested_quantity
        # TODO: call super().__init__() with a useful message


# TODO: raise OutOfStockError("Widget", 10) inside try/except
# TODO: in the except block, print error.item_name and error.requested_quantity
