class NegativeAgeError(Exception):
    pass


def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")
    return age


try:
    set_age(-5)
except NegativeAgeError as error:
    print(error)
