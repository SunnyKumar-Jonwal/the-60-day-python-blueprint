class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Car(Vehicle):
    pass


car = Car("Toyota", "Corolla")
print(car.make)
print(car.model)
