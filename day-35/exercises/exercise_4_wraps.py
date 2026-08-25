# TODO: import wraps from functools


def announce(func):
    # TODO: add @wraps(func) here, right above "def wrapper(*args, **kwargs):"
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result

    return wrapper


@announce
def add(a, b):
    return a + b


# TODO: print add.__name__ to see that @wraps(func) preserved it as "add"
