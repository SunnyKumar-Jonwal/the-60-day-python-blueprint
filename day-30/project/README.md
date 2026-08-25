# Bank Account Simulator — Day 30 mini-project

A command-line bank account simulator: create savings and checking accounts,
deposit, withdraw, and apply interest, all in memory for the duration of one
run.

## Setup

Nothing beyond the repo's root setup (see the [root README](../../README.md)) —
this project uses only the Python standard library.

## Run it

From the **repository root**:

```bash
python day-30/project/bank_simulator.py
```

Accounts exist only in memory for the current run — unlike Day 20's contact
book, this project doesn't persist to a file (see the stretch goal below if
you want to add that).

## Sample session

```
1. Create account
2. Deposit
3. Withdraw
4. Apply interest (savings only)
5. List accounts
6. Exit
Choose an option: 1
Owner name: Ada
Initial balance: 500
Account type (savings/checking): savings
Interest rate (e.g. 0.05 for 5%): 0.05
Created Ada's SavingsAccount: $500.00

1. Create account
2. Deposit
3. Withdraw
4. Apply interest (savings only)
5. List accounts
6. Exit
Choose an option: 1
Owner name: Bob
Initial balance: 200
Account type (savings/checking): checking
Overdraft limit: 100
Created Bob's CheckingAccount: $200.00

1. Create account
2. Deposit
3. Withdraw
4. Apply interest (savings only)
5. List accounts
6. Exit
Choose an option: 3
Owner name: Bob
Amount to withdraw: 250
New balance: $-50.00

1. Create account
2. Deposit
3. Withdraw
4. Apply interest (savings only)
5. List accounts
6. Exit
Choose an option: 3
Owner name: Ada
Amount to withdraw: 10000
Error: Cannot withdraw 10000.00: balance is only 500.00

1. Create account
2. Deposit
3. Withdraw
4. Apply interest (savings only)
5. List accounts
6. Exit
Choose an option: 4
Owner name: Ada
Applied $25.00 interest. New balance: $525.00

1. Create account
2. Deposit
3. Withdraw
4. Apply interest (savings only)
5. List accounts
6. Exit
Choose an option: 6
Goodbye!
```

Note how **withdrawing $250 from Bob's checking account succeeds** even
though his balance is only $200 — `CheckingAccount.withdraw()` allows going
negative up to its `overdraft_limit`, which is exactly the polymorphism this
project is built around: the same `withdraw()` call behaves differently
depending on the account's actual class.

## How it's built

- `BankAccount` — the base class. `balance` is a read-only `@property`
  (Day 25) backed by `_balance`; the only way to change it is through
  `deposit()`/`withdraw()`, which validate the amount.
- `SavingsAccount(BankAccount)` and `CheckingAccount(BankAccount)` — each adds
  its own attribute (`interest_rate`, `overdraft_limit`) via `super().__init__()`
  (Day 23). `CheckingAccount` **overrides** `withdraw()` entirely (Day 24) to
  allow overdrafts.
- `BankError`, `InvalidAmountError`, `InsufficientFundsError` — a small custom
  exception hierarchy (Day 29); the CLI catches them specifically to show a
  clean error message instead of crashing.
- `__str__`, `__repr__`, `__eq__` (Days 26-27) — printing an account, or a
  list of them, gives readable output.
- `main()` — a menu loop identical in spirit to Day 20's contact book, but now
  operating on real objects instead of dicts.

## Stretch goal

Pick one (or more) to extend the project once the core works:

- **Persistence**: save and load accounts to a file (reuse Module 2's file
  handling) — you'll need a way to serialize which subclass each account is,
  not just its data.
- **Transfer between accounts**: add a menu option that withdraws from one
  account and deposits into another, rolling back the withdrawal if the
  deposit somehow fails.
- **Transaction history**: give `BankAccount` a `history` list that records
  every deposit/withdrawal, and a menu option to print one account's history.
- **A `BusinessAccount` subclass**: add a third account type with its own
  rules (e.g. a flat monthly fee applied via a new method).
