point = (3, 4)
print(point[0])
print(point[-1])

x, y = point
print(x, y)

name, age = "Ada", 30
print(name, age)


def min_max(numbers):
    return min(numbers), max(numbers)


lowest, highest = min_max([3, 1, 4, 1, 5])
print(lowest, highest)

colors = ("red", "green", "blue")
print(colors)
