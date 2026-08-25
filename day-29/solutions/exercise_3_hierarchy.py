class ValidationError(Exception):
    pass


class TooShortError(ValidationError):
    pass


class TooLongError(ValidationError):
    pass


try:
    raise TooShortError("Too short!")
except ValidationError as error:
    print(error)
