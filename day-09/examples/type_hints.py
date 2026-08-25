age: int = 30
name: str = "Ada"
price: float = 19.99


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


print(age, name, price)
print(add(3, 4))
print(greet("Ada"))
print(greet("Ada", "Hi"))
