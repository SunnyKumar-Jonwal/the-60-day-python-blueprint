# Day 30: Milestone — Bank Account Simulator (mini-project)

**Module:** 3 — OOP

## What you're building

A command-line **bank account simulator**: create savings and checking
accounts, deposit, withdraw, and apply interest — all backed by real classes
instead of plain dicts, with proper validation via custom exceptions.

Full instructions, code, and a stretch goal live in [`project/`](project/) —
start there.

## What this exercises

- **Classes & objects** ([Day 21](../day-21/README.md)) — `BankAccount` as the
  core blueprint.
- **Encapsulation** ([Day 25](../day-25/README.md)) — `balance` is a
  `@property` backed by `_balance`, never set directly.
- **Inheritance & polymorphism** ([Days 23](../day-23/README.md)-[24](../day-24/README.md))
  — `SavingsAccount` and `CheckingAccount` both extend `BankAccount`, and
  `CheckingAccount` overrides `withdraw()` to allow overdrafts.
- **Dunder methods** ([Days 26](../day-26/README.md)-[27](../day-27/README.md))
  — `__str__`, `__repr__`, and `__eq__` on `BankAccount`.
- **Custom exceptions** ([Day 29](../day-29/README.md)) — `InsufficientFundsError`
  and `InvalidAmountError`, both under a shared `BankError` base.

## Run it

```bash
python day-30/project/bank_simulator.py
```

See [`project/README.md`](project/README.md) for the full write-up, sample
session, and the stretch goal.
