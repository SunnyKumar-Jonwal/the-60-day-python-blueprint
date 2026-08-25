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

cursor.execute("UPDATE contacts SET email = ? WHERE name = ?", ("ada@newmail.com", "Ada"))
connection.commit()
cursor.execute("SELECT * FROM contacts")
print(cursor.fetchall())

cursor.execute("DELETE FROM contacts WHERE name = ?", ("Grace",))
connection.commit()
cursor.execute("SELECT * FROM contacts")
print(cursor.fetchall())

connection.close()
