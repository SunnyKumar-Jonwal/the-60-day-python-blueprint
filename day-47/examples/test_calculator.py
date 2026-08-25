import pytest


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_normal_case():
    assert divide(10, 2) == 5


@pytest.fixture
def sample_numbers():
    return [4, 8, 15, 16, 23, 42]


def test_sum(sample_numbers):
    assert sum(sample_numbers) == 108


def test_length(sample_numbers):
    assert len(sample_numbers) == 6
