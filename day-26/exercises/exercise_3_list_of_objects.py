class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"


# TODO: create a list of three Product instances
# TODO: print the list directly (not a loop) -- observe __repr__ is used for each item
