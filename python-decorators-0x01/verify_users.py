#!/usr/bin/python3

import sqlite3


connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()



print("User Table: ")
for row in rows:
    print(row)

connection.close()