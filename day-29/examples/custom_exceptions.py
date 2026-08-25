class BankError(Exception):
    """Base class for every error this bank account module can raise."""


class InsufficientFundsError(BankError):
    def __init__(self, balance, amount_requested):
        self.balance = balance
        self.amount_requested = amount_requested
        message = f"Cannot withdraw {amount_requested}: balance is only {balance}"
        super().__init__(message)


class InvalidAmountError(BankError):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


try:
    withdraw(100, 500)
except InsufficientFundsError as error:
    print(error)
    print(error.amount_requested)

try:
    raise InvalidAmountError("Amount must be positive")
except BankError as error:
    print(f"Bank error: {error}")
