# Day 50: Milestone — Weather Data Analysis (mini-project)

**Module:** 5 — Real-World Libraries

## What you're building

A small **data analysis project**: load a CSV of daily weather readings for
three cities into pandas, compute summary statistics, print a report, and
back it all with real pytest tests.

Full instructions, code, and a stretch goal live in [`project/`](project/) —
start there.

## What this exercises

- **pandas** ([Days 45](../day-45/README.md)-[46](../day-46/README.md)) —
  `read_csv`, `groupby`, filtering, and aggregation.
- **pytest** ([Day 47](../day-47/README.md)) — a `@pytest.fixture` providing
  sample data, and multiple `test_*` functions checking the analysis
  functions against hand-computed expected values.
- **Separation of I/O from logic** — `analysis.py`'s functions take a
  DataFrame as an argument rather than reading the file themselves, which is
  exactly what makes them testable without touching the real CSV.

## Run it

```bash
python day-50/project/report.py
pytest day-50/project/ -v
```

See [`project/README.md`](project/README.md) for the full write-up, sample
output, and the stretch goal.
