from functools import wraps


def shout(func):
    def wrapper():
        return func().upper()

    return wrapper


@shout
def greet():
    return "hello"


print(greet())


def my_function(*args, **kwargs):
    print(args)
    print(kwargs)


my_function(1, 2, name="Ada")


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


add(3, 4)
print(add.__name__)
