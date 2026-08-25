class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"

    # TODO: add __repr__ that returns "Product(name='{name}', price={price})"


product = Product("Mug", 9.99)
# TODO: print(repr(product))
