#!/usr/bin/python3

from datetime import datetime
import functools
import sqlite3


#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time = datetime.now()
        query = kwargs.get("query")
        print(f"[LOG] Executing SQL: {query}, Ex@:{time}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print(users)