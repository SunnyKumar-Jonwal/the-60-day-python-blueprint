import sqlite3

connection = sqlite3.connect("day-54/examples/example.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    )
""")
connection.commit()

cursor.execute(
    "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
    ("Dune", "Frank Herbert", 1965),
)
cursor.execute(
    "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
    ("1984", "George Orwell", 1949),
)
connection.commit()

cursor.execute("SELECT * FROM books")
print(cursor.fetchall())

cursor.execute("SELECT * FROM books WHERE year > ?", (1950,))
print(cursor.fetchall())

cursor.execute("SELECT * FROM books WHERE id = ?", (1,))
print(cursor.fetchone())

cursor.execute("UPDATE books SET year = ? WHERE title = ?", (1966, "Dune"))
connection.commit()
cursor.execute("SELECT * FROM books WHERE title = ?", ("Dune",))
print(cursor.fetchone())

cursor.execute("DELETE FROM books WHERE title = ?", ("1984",))
connection.commit()
cursor.execute("SELECT * FROM books")
print(cursor.fetchall())

connection.close()
