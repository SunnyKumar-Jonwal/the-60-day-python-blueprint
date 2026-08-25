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
def always_fails():
    raise ValueError("nope")


try:
    always_fails()
except ValueError:
    print("Gave up.")
