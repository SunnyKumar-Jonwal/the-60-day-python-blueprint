class Shape:
    def describe(self):
        return "I am a shape."


class Square(Shape):
    def describe(self):
        return "I am a square."


class Circle(Shape):
    def describe(self):
        return "I am a circle."


square = Square()
circle = Circle()
print(square.describe())
print(circle.describe())
