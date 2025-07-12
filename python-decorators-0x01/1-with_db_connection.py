#!/usr/bin/python3
"""
Handle Database Connections with a Decorator
Objective: create a decorator,
that automatically handles opening
and
closing database connections
"""


from datetime import datetime
import functools
import sqlite3 


def with_db_connection(func):
    """
    a decorator with_db_connection that opens a database connection,
    passes it to the function and closes it afterword

    _summary_
    Args:
        func (function): get_user_by_id

    Returns:
        fucntion: wrapper
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if "user_id" not in kwargs and (len(args) < 1):
            raise ValueError("Missing required argument: user_id")
        connection = sqlite3.connect('users.db')
        try:
            return func(connection, *args, **kwargs)
        finally:
            connection.close()
    return wrapper


@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)