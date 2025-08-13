"""Write a Python program to connect to an SQLite3 database, create a table, insert data, and
fetch data."""

import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)

conn.commit()
conn.close()
