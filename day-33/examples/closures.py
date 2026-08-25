def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"

    return greet


hello_greeter = make_greeter("Hello")
hey_greeter = make_greeter("Hey")

print(hello_greeter("Ada"))
print(hey_greeter("Ada"))


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(counter())
print(counter())
print(counter())
