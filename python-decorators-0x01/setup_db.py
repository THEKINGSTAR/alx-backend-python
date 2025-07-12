#!/usr/bin/python3
"""
SQLite3 setup with a users table, suitable for quick testing or prototyping
"""

import sqlite3

# Connect to SQLite (creates file if it doesn't exist)
connection = sqlite3.connect("users.db")
cursor = connection.cursor()


# Drop if exists (for repeat runs)
cursor.execute("DROP TABLE IF EXISTS users")

# Create table
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert some test data
users = [
    ("alice", "alice@example.com", 25),
    ("bob", "bob@example.com", 30),
    ("charlie", "charlie@example.com", 22)
]


cursor.executemany("INSERT INTO users (username, email, age) VALUES (?, ?, ?)", users)

# Save and close
connection.commit()
connection.close()

print("✅ SQLite database and users table created.")