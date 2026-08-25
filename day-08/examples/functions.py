def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


def add(a, b):
    return a + b


greet("Ada")
greet("Ada", "Hi")
greet("Ada", greeting="Hey")

result = add(3, 4)
print(result)
