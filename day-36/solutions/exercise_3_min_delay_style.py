def require_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError(f"Argument {arg} must not be negative")
        return func(*args, **kwargs)

    return wrapper


@require_positive
def add(a, b):
    return a + b


try:
    print(add(3, 4))
except ValueError as error:
    print(error)

try:
    print(add(-3, 4))
except ValueError as error:
    print(error)
