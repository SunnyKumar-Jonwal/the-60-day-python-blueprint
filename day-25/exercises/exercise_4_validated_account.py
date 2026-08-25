class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    # TODO: add a @balance.setter that raises ValueError if value < 0,
    # otherwise sets self._balance = value


# TODO: create a BankAccount(200), set .balance = 300, then print .balance
