def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


try:
    print(set_age(25))
except ValueError as error:
    print(error)

try:
    print(set_age(-5))
except ValueError as error:
    print(error)
