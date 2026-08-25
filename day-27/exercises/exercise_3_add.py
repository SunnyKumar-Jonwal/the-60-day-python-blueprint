class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # TODO: add __add__ that returns a new Vector with x and y summed componentwise


v1 = Vector(1, 2)
v2 = Vector(3, 4)
# TODO: print(v1 + v2)  -- should be Vector(4, 6)
