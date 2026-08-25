class ValidationError(Exception):
    pass


class TooShortError(ValidationError):
    pass


class TooLongError(ValidationError):
    pass


def validate_password(password):
    if len(password) < 8:
        raise TooShortError("Password is too short")
    if len(password) > 64:
        raise TooLongError("Password is too long")
    return password


try:
    print(validate_password("longenoughpassword"))
except ValidationError as error:
    print(error)

try:
    print(validate_password("short"))
except ValidationError as error:
    print(error)
