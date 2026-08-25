# Day 48: Logging

**Module:** 5 — Real-World Libraries

## What you'll learn

- Why `print()` isn't enough for a real program
- The `logging` module and log levels
- Configuring a logger with `basicConfig`
- Logging to a file instead of (or as well as) the console

## Explanation

### Why not just `print()`?

You've used `print()` all course long, and it's fine for learning and small
scripts. But it has real limits in a bigger program:

- No way to say "this message is just informational" vs. "this is a
  serious problem" — every `print()` looks equally important.
- No easy way to turn messages on/off by severity without deleting or
  commenting out `print()` calls.
- No built-in way to route messages to a file, without doing your own file
  handling (Day 17-18) around every message.

The **`logging`** module (standard library, `import logging`) solves all
three.

### Log levels

From least to most severe:

| Level | When to use it |
|---|---|
| `DEBUG` | Detailed info, useful only while actively debugging |
| `INFO` | Confirmation that things are working as expected |
| `WARNING` | Something unexpected happened, but the program can continue |
| `ERROR` | A real problem — something failed |
| `CRITICAL` | A severe problem — the program may be unable to continue |

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("This won't show -- DEBUG is below the configured INFO level")
logging.info("Starting the process")
logging.warning("Config file not found, using defaults")
logging.error("Failed to connect to the database")
logging.critical("Out of memory, shutting down")
```

Setting `level=logging.INFO` means: show `INFO` and everything *more*
severe (`WARNING`, `ERROR`, `CRITICAL`), but suppress anything less severe
(`DEBUG`). This is the mechanism that solves `print()`'s "no way to turn
things on/off" problem — change one line, and every `logging.debug(...)`
call across your whole program goes quiet without deleting any of them.

### Formatting log messages

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logging.info("Server started")
# 2024-08-25 14:30:05,123 [INFO] Server started
```

`%(asctime)s`, `%(levelname)s`, `%(message)s` are placeholders `basicConfig`
fills in automatically for every log call — timestamp, level name, and your
actual message.

### Logging to a file

```python
import logging

file_logger = logging.getLogger("file_demo")
file_logger.setLevel(logging.INFO)
file_logger.propagate = False   # don't also send these up to root's console handler
handler = logging.FileHandler("day-48/examples_app.log")
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
file_logger.addHandler(handler)

file_logger.info("This goes to the file, not the console")
```

This uses a **named logger with its own handler** rather than a second
`basicConfig()` call — see the gotcha below for why. By default, a logger's
messages **also** propagate up to the root logger and get handled by its
handlers too (so without `propagate = False`, this message would show on the
console *and* be written to the file) — setting `propagate = False` keeps
this logger's output confined to its own handler.

### Named loggers

Real projects usually create a named logger per module instead of using the
bare `logging.info(...)` functions directly, so log messages show *where*
they came from:

```python
import logging

logger = logging.getLogger(__name__)   # __name__ from Day 37 -- names the logger after this file
logger.setLevel(logging.INFO)

logger.info("Using a named logger")
```

## Worked example

See [`examples/logging_basics.py`](examples/logging_basics.py). Run it with:

```bash
python day-48/examples/logging_basics.py
```

## Exercises

1. **`exercise_1_levels.py`** — configure logging at `WARNING` level, and log
   one message at each of the five levels; observe that only `WARNING` and
   above print.
2. **`exercise_2_format.py`** — configure logging with a format string
   including the level name and message, and log a couple of messages.
3. **`exercise_3_file_logging.py`** — configure logging to write to
   `day-48/exercises_app.log` instead of the console, log a few messages, then
   read the file back and print its contents.
4. **`exercise_4_named_logger.py`** — create a named logger with
   `logging.getLogger(__name__)`, and log an `INFO` and a `WARNING` message
   through it.

## Common Gotchas

- **`basicConfig()` only works once per process.** If it's already been
  called (even implicitly, by an earlier `logging.info()` call using the
  default config), a later `basicConfig()` call with different settings is
  silently ignored — this trips people up constantly. To reconfigure the
  level later in the same script, call `logging.getLogger().setLevel(...)`
  instead; to add file output alongside console output, add a separate named
  logger with its own `FileHandler` (as in the file-logging example above)
  rather than calling `basicConfig()` a second time.
- **Setting the level too high and wondering why nothing shows.** The
  default level (with no `basicConfig` call at all) is `WARNING` — `logging.
  info(...)` and `logging.debug(...)` calls produce nothing until you
  explicitly lower the level.
- **Using `logging.error(...)` for things that aren't actually errors.**
  Reserve `ERROR`/`CRITICAL` for genuine failures — overusing them makes real
  problems harder to spot in a sea of noise.
- **Forgetting logs written to a file need `with`-free cleanup.** Unlike
  Day 17-18's manual file handling, `logging` manages its own file handles —
  you don't (and shouldn't) `open()`/`close()` the log file yourself.
