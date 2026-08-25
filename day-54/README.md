# Day 54: SQLite basics

**Module:** 6 — Web APIs & Capstone

## What you'll learn

- What SQLite is, and why it's a good fit for learning databases
- Connecting, creating a table, and closing a connection
- `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- Parameterized queries, and why they matter for security

## Explanation

### What SQLite is

Every day so far that needed persistence used plain text/CSV files (Days
17-19) or JSON (Day 42). A **database** is built specifically for storing,
querying, and updating structured data efficiently, especially as it grows.
**SQLite** is a database engine that stores an entire database in a single
file on disk — no separate server process to install or run, which makes it
ideal for learning (and for genuinely many small-to-medium real projects).
It's part of Python's standard library: `import sqlite3`, no `pip install`
needed.

**SQL** (Structured Query Language) is the language you use to talk to a
relational database like SQLite — a handful of commands (`CREATE TABLE`,
`INSERT`, `SELECT`, `UPDATE`, `DELETE`) cover almost everything today.

### Connecting and creating a table

```python
import sqlite3

connection = sqlite3.connect("day-54/examples/example.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    )
""")
connection.commit()
```

- `connect(path)` opens (or creates, if missing) a database file.
- A **cursor** is what you use to actually run SQL commands and fetch
  results.
- `IF NOT EXISTS` means running this twice doesn't error the second time.
- `commit()` saves your changes — without it, writes stay uncommitted and
  can be lost.

### Inserting data

```python
cursor.execute(
    "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
    ("Dune", "Frank Herbert", 1965),
)
connection.commit()
```

The `?` placeholders and the tuple of values are a **parameterized query** —
always build queries this way when a value comes from a variable, **never**
with an f-string:

```python
# NEVER do this:
cursor.execute(f"INSERT INTO books (title) VALUES ('{title}')")
```

Building SQL by string-formatting user-supplied values opens the door to
**SQL injection** — a malicious value like `title = "x'); DROP TABLE books;--"`
can execute arbitrary SQL you never intended. Parameterized queries (`?`
placeholders) make the database treat the value purely as data, never as
part of the SQL command itself — this is not optional in real code.

### Querying data

```python
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()   # a list of all matching rows
print(rows)   # [(1, 'Dune', 'Frank Herbert', 1965)] -- each row is a tuple

cursor.execute("SELECT * FROM books WHERE year > ?", (1960,))
recent = cursor.fetchall()

cursor.execute("SELECT * FROM books WHERE id = ?", (1,))
one_book = cursor.fetchone()   # a single row (or None if no match), instead of a list
```

### Updating and deleting

```python
cursor.execute("UPDATE books SET year = ? WHERE title = ?", (1966, "Dune"))
connection.commit()

cursor.execute("DELETE FROM books WHERE id = ?", (1,))
connection.commit()
```

### Closing the connection

```python
connection.close()
```

`sqlite3.connect(...)` can also be used as a context manager (`with
sqlite3.connect(...) as connection:`), but unlike file `with` (Day 18), it
**only** auto-commits (or rolls back on an error) — it does **not** close
the connection for you. You still need an explicit `connection.close()`, or
nest it inside your own cleanup.

## Worked example

See [`examples/sqlite_basics.py`](examples/sqlite_basics.py). Run it with:

```bash
python day-54/examples/sqlite_basics.py
```

## Exercises

1. **`exercise_1_create_insert.py`** — create a `contacts` table (`id`,
   `name`, `email`) and insert two rows.
2. **`exercise_2_select.py`** — query all rows from `contacts` and print
   them, then query for just one by `id`.
3. **`exercise_3_update_delete.py`** — update one contact's email, then
   delete the other contact, printing the table's contents after each step.
4. **`exercise_4_parameterized.py`** — write a function `find_by_name(name)`
   that safely queries `contacts` by name using a parameterized query.

## Common Gotchas

- **Building SQL with f-strings/`+` instead of `?` placeholders.** This is a
  genuine security vulnerability (SQL injection), not just a style
  preference — always use parameterized queries for any value that isn't a
  hardcoded literal.
- **Forgetting `commit()`.** Without it, `INSERT`/`UPDATE`/`DELETE` changes
  may not actually be saved to the file — especially easy to miss since
  `SELECT` within the same connection can still "see" uncommitted changes,
  masking the problem until you reconnect.
- **The single-value tuple trap.** `cursor.execute("... WHERE id = ?", (1))`
  is a bug — `(1)` is just the int `1` in parentheses, not a tuple; it needs
  a trailing comma: `(1,)`. Exactly the same rule as Day 12's one-item
  tuples.
- **Forgetting `connection.close()`.** `with sqlite3.connect(...)` handles
  commit/rollback but not closing — leaving connections open can eventually
  exhaust available file handles in a long-running program.
