import pytest


@pytest.fixture
def sample_list():
    return [10, 20, 30, 40]


def test_sum_fixture(sample_list):
    assert sum(sample_list) == 100


def test_max_fixture(sample_list):
    assert max(sample_list) == 40
