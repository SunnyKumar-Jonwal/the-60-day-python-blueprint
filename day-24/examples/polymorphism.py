class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Duck:
    def speak(self):
        return "Quack!"


animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(animal.speak())


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2


shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(shape.area())
