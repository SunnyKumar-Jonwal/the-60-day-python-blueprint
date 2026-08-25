def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


# TODO: import pytest
# TODO: write test_withdraw_too_much_raises() that uses "with pytest.raises(ValueError):"
# around a call to withdraw(100, 500)
