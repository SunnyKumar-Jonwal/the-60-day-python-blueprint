class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"


product = Product("Mug", 9.99)
print(repr(product))
