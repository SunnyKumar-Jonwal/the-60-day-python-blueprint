import pytest


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


def test_withdraw_too_much_raises():
    with pytest.raises(ValueError):
        withdraw(100, 500)
