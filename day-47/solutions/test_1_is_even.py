def is_even(n):
    return n % 2 == 0


def test_is_even_with_even_number():
    assert is_even(4) is True


def test_is_even_with_odd_number():
    assert is_even(7) is False
