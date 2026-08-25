import sqlite3

connection = sqlite3.connect("day-54/exercises/exercise.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS contacts")
cursor.execute("""
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")
cursor.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", ("Ada", "ada@example.com"))
cursor.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", ("Grace", "grace@example.com"))
connection.commit()

# TODO: query all rows from contacts and print them
# TODO: query for just the contact with id = 1 and print it (use fetchone())

connection.close()
