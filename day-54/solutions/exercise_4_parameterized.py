import sqlite3

connection = sqlite3.connect("day-54/solutions/exercise.db")
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
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    return cursor.fetchone()


print(find_by_name("Grace"))

connection.close()
