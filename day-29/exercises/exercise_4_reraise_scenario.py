class ValidationError(Exception):
    pass


class TooShortError(ValidationError):
    pass


class TooLongError(ValidationError):
    pass


def validate_password(password):
    pass
    # TODO: raise TooShortError if len(password) < 8
    # TODO: raise TooLongError if len(password) > 64
    # TODO: otherwise return password


# TODO: call validate_password("longenoughpassword") inside try/except, print success
# TODO: call validate_password("short") inside try/except, print the caught error
