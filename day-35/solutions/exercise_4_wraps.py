from functools import wraps


def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result

    return wrapper


@announce
def add(a, b):
    return a + b


print(add.__name__)
