"""Write a Python program to insert data into an SQLite3 database and fetch it."""

import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("David", 16, "10th"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Eva", 15, "9th"))

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
