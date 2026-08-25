class Shape:
    def area(self):
        raise NotImplementedError


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


shapes = [Triangle(4, 6), Square(5)]


def total_area(shapes):
    return sum([shape.area() for shape in shapes])


print(total_area(shapes))
