def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Ada")


def retry(attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except ValueError as error:
                    last_error = error
                    print(f"Attempt {attempt} failed: {error}")
            raise last_error

        return wrapper

    return decorator


@retry(3)
def flaky_function():
    raise ValueError("Something went wrong")


try:
    flaky_function()
except ValueError:
    print("Gave up after 3 attempts.")
