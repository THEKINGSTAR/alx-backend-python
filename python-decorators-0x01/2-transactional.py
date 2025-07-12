#!/usr/bin/python3
"""
Transaction Management Decorator (mandatory)
Objective: create a decorator that manages database transactions
by automatically committing or rolling back changes
"""


from datetime import datetime
import sqlite3 
import functools


def transactional(fucn):
    """
    a decorator that ensures a function
    running a database operation is wrapped
    inside a transaction.
    If the function raises an error,
    rollback;
    otherwise commit the transaction.
    """
    @functools.wraps(fucn)
    def wrapper(connection, *args, **kwargs):
        time = datetime.now()
        try:
            result = fucn(connection, *args, **kwargs)
            connection.commit()
            print(f"[LOG] Transition Commited @:{time}")
        except Exception as e:
            connection.rollback()
            print(f"[ERROR] Transaction rolled back due to: {e} @{time}")
            raise
    return wrapper

        



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
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')