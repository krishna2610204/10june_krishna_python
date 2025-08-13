"""Write a Python program to create a database and a table using
SQLite3."""

import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT
)
""")

cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Alice", 14, "8th"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Bob", 15, "9th"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Charlie", 13, "7th"))

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
