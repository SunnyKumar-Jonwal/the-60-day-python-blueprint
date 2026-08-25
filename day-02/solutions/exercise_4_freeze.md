# Exercise 4: Freeze your dependencies — solution

```bash
pip freeze > frozen.txt
```

`frozen.txt` should contain `requests==<version>` plus its dependencies, each pinned
to an exact version — this is the same format used in this repo's root
`requirements.txt`.
