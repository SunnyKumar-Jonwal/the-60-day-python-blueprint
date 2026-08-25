class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"


products = [Product("Mug", 9.99), Product("Pen", 1.5), Product("Notebook", 4.0)]
print(products)
