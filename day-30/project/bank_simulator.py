class BankError(Exception):
    """Base class for every error this bank account module can raise."""


class InvalidAmountError(BankError):
    pass


class InsufficientFundsError(BankError):
    def __init__(self, balance, amount_requested):
        self.balance = balance
        self.amount_requested = amount_requested
        message = f"Cannot withdraw {amount_requested:.2f}: balance is only {balance:.2f}"
        super().__init__(message)


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount

    def __str__(self):
        return f"{self.owner}'s {self.__class__.__name__}: ${self._balance:.2f}"

    def __repr__(self):
        return f"{self.__class__.__name__}(owner={self.owner!r}, balance={self._balance:.2f})"

    def __eq__(self, other):
        return self.owner == other.owner and self._balance == other._balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        return interest


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0.0, overdraft_limit=100.0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > self._balance + self.overdraft_limit:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount


def find_account(accounts, owner):
    for account in accounts:
        if account.owner.lower() == owner.lower():
            return account
    return None


def create_account(accounts):
    owner = input("Owner name: ").strip()
    balance = float(input("Initial balance: ").strip())
    account_type = input("Account type (savings/checking): ").strip().lower()

    if account_type == "savings":
        rate = float(input("Interest rate (e.g. 0.05 for 5%): ").strip())
        account = SavingsAccount(owner, balance, rate)
    elif account_type == "checking":
        overdraft = float(input("Overdraft limit: ").strip())
        account = CheckingAccount(owner, balance, overdraft)
    else:
        print("Unknown account type.")
        return

    accounts.append(account)
    print(f"Created {account}")


def deposit(accounts):
    account = find_account(accounts, input("Owner name: ").strip())
    if account is None:
        print("Account not found.")
        return

    amount = float(input("Amount to deposit: ").strip())
    try:
        account.deposit(amount)
        print(f"New balance: ${account.balance:.2f}")
    except InvalidAmountError as error:
        print(f"Error: {error}")


def withdraw(accounts):
    account = find_account(accounts, input("Owner name: ").strip())
    if account is None:
        print("Account not found.")
        return

    amount = float(input("Amount to withdraw: ").strip())
    try:
        account.withdraw(amount)
        print(f"New balance: ${account.balance:.2f}")
    except (InvalidAmountError, InsufficientFundsError) as error:
        print(f"Error: {error}")


def apply_interest(accounts):
    account = find_account(accounts, input("Owner name: ").strip())
    if account is None:
        print("Account not found.")
        return
    if not isinstance(account, SavingsAccount):
        print(f"{account.owner}'s account does not earn interest.")
        return

    interest = account.apply_interest()
    print(f"Applied ${interest:.2f} interest. New balance: ${account.balance:.2f}")


def list_accounts(accounts):
    if not accounts:
        print("No accounts yet.")
        return
    for account in accounts:
        print(account)


def print_menu():
    print("\n1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Apply interest (savings only)")
    print("5. List accounts")
    print("6. Exit")


def main():
    accounts = []
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            apply_interest(accounts)
        elif choice == "5":
            list_accounts(accounts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


main()
