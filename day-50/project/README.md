# Weather Data Analysis — Day 50 mini-project

A pandas-based analysis of 10 days of weather readings across three cities,
with a runnable report script and a real pytest test suite.

## Setup

Nothing beyond the repo's root setup (see the [root README](../../README.md)) —
`pandas` and `pytest` are already in the root `requirements.txt`.

## Run it

From the **repository root**:

```bash
python day-50/project/report.py
pytest day-50/project/ -v
```

## Sample output

```
=== Average temperature by city (C) ===
city
Austin     31.2
Miami      30.8
Seattle    18.0
Name: temperature_c, dtype: float64

=== Hottest day ===
Austin on 2024-06-07: 34.0C

=== Total precipitation by city (mm) ===
city
Austin      16.5
Miami      133.5
Seattle     35.0
Name: precipitation_mm, dtype: float64

=== Days above 30C ===
Austin: 7
Seattle: 0
Miami: 8
```

```
$ pytest day-50/project/ -v
day-50/project/test_analysis.py::test_average_temperature_by_city PASSED
day-50/project/test_analysis.py::test_hottest_day PASSED
day-50/project/test_analysis.py::test_total_precipitation_by_city PASSED
day-50/project/test_analysis.py::test_days_above_threshold PASSED
day-50/project/test_analysis.py::test_days_above_threshold_with_no_matches PASSED

5 passed
```

## How it's built

- [`weather.csv`](weather.csv) — 30 rows: 10 days × 3 cities (Austin,
  Seattle, Miami), with temperature, humidity, and precipitation.
- [`analysis.py`](analysis.py) — pure functions that take a `DataFrame` as
  an argument and return a result (Day 45-46's `groupby`, boolean filtering,
  and aggregation). None of these functions read the file themselves — that
  separation is exactly what makes them easy to test.
- [`report.py`](report.py) — the runnable script: loads `weather.csv` via
  `analysis.load_weather()`, then calls each analysis function and prints
  the results.
- [`test_analysis.py`](test_analysis.py) — a `@pytest.fixture` (Day 47)
  providing a small, hand-built sample `DataFrame` with known values, and
  five `test_*` functions asserting the analysis functions produce the
  correct result against that known data. Testing against a small fixture
  rather than the real `weather.csv` means the tests keep passing even if
  the sample dataset changes later.

## Stretch goal

Pick one (or more) to extend the project once the core works:

- **A `coldest_day()` function**, mirroring `hottest_day()`, plus a test for
  it.
- **A `--city` command-line flag** (Day 40's `argparse`) on `report.py` that
  filters the report to just one city.
- **Correlation**: use `df["temperature_c"].corr(df["precipitation_mm"])` to
  check whether hotter days tend to have less rain in this dataset, and add
  it to the report.
- **A rolling average**: add a function computing each city's 3-day rolling
  average temperature (`df.groupby("city")["temperature_c"].rolling(3).mean()`),
  with a test using a small fixture where you've hand-computed the expected
  values.
