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


def find_by_name(name):
    pass
    # TODO: use a parameterized query (WHERE name = ?) to find a contact by
    # name, and return the result of fetchone()


# TODO: print find_by_name("Grace")

connection.close()
