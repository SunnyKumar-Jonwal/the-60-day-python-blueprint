# Exercise 3: Freeze before and after — solution

```bash
pip freeze
pip install six
pip freeze
```

The second `pip freeze` output has one extra line: `six==<version>`, that
wasn't present in the first.
