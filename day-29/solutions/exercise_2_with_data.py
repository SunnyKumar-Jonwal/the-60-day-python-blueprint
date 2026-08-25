class OutOfStockError(Exception):
    def __init__(self, item_name, requested_quantity):
        self.item_name = item_name
        self.requested_quantity = requested_quantity
        message = f"Not enough stock for '{item_name}' (requested {requested_quantity})"
        super().__init__(message)


try:
    raise OutOfStockError("Widget", 10)
except OutOfStockError as error:
    print(error.item_name)
    print(error.requested_quantity)
