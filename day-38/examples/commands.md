# pip & venv command walk-through

Run these in a **scratch** virtual environment, not this repo's own `venv/`.

```bash
mkdir scratch && cd scratch
python -m venv venv
source venv/bin/activate   # or venv\Scripts\Activate.ps1 on Windows PowerShell
```

## Install a pinned version

```bash
pip install requests==2.31.0
```

```
Collecting requests==2.31.0
...
Successfully installed requests-2.31.0 ...
```

## Inspect it

```bash
pip show requests
```

```
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
...
```

```bash
pip list
```

```
Package            Version
------------------ -------
certifi            2024.2.2
charset-normalizer 3.3.2
idna               3.6
pip                24.0
requests           2.31.0
urllib3            2.2.1
```

## Freeze the environment

```bash
pip freeze
```

```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
```

## Upgrade

```bash
pip install --upgrade requests
```

```
Successfully installed requests-2.32.3
```

## Uninstall

```bash
pip uninstall requests
```

```
Proceed (y/n)? y
Successfully uninstalled requests-2.32.3
```

```bash
pip list
```

`requests` no longer appears (its dependencies like `certifi` may remain
unless uninstalled too — `pip` doesn't remove dependencies automatically).
