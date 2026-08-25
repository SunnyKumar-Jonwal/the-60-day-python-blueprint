import sqlite3

connection = sqlite3.connect("day-54/exercises/exercise.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS contacts")

# TODO: create a "contacts" table with columns id (INTEGER PRIMARY KEY
# AUTOINCREMENT), name (TEXT NOT NULL), email (TEXT NOT NULL)
# TODO: commit
# TODO: insert two contacts using parameterized queries, then commit

connection.close()
