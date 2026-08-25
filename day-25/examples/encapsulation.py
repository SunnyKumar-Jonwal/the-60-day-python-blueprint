class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        self.__account_number = "42"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def show_account_number(self):
        return self.__account_number


account = BankAccount(100)
print(account.balance)

account.balance = 150
print(account.balance)

print(account.show_account_number())
# account.balance = -50 would raise ValueError -- not run here, see Day 28 for
# how to catch it safely
