import pandas as pd
import pytest
from analysis import (
    average_temperature_by_city,
    days_above_threshold,
    hottest_day,
    total_precipitation_by_city,
)


@pytest.fixture
def sample_weather():
    return pd.DataFrame(
        {
            "date": ["2024-06-01", "2024-06-01", "2024-06-02", "2024-06-02"],
            "city": ["Austin", "Seattle", "Austin", "Seattle"],
            "temperature_c": [30.0, 18.0, 32.0, 17.0],
            "precipitation_mm": [0.0, 5.0, 0.0, 8.0],
        }
    )


def test_average_temperature_by_city(sample_weather):
    averages = average_temperature_by_city(sample_weather)
    assert averages["Austin"] == 31.0
    assert averages["Seattle"] == 17.5


def test_hottest_day(sample_weather):
    hottest = hottest_day(sample_weather)
    assert hottest["city"] == "Austin"
    assert hottest["temperature_c"] == 32.0


def test_total_precipitation_by_city(sample_weather):
    totals = total_precipitation_by_city(sample_weather)
    assert totals["Austin"] == 0.0
    assert totals["Seattle"] == 13.0


def test_days_above_threshold(sample_weather):
    assert days_above_threshold(sample_weather, "Austin", 25) == 2
    assert days_above_threshold(sample_weather, "Seattle", 25) == 0


def test_days_above_threshold_with_no_matches(sample_weather):
    assert days_above_threshold(sample_weather, "Seattle", 100) == 0
