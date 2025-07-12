#!/usr/bin/python3
"""
Using Decorators to retry database queries (mandatory)
Objective: create a decorator that retries database operations
if they fail due to transient errors
"""


from datetime import datetime
import functools
import time
import sqlite3 


#### paste your with_db_decorator here
def retry_on_failure(retries=3, delay=1):
    """
    decorator that retries the function
    of a certain number of times if it raises an exception
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapers(connection, *args, **kwargs):
            for attempt in range(1, retries + 1):
                time_stamp = datetime.now()
                try:
                    result = func(connection, *args, **kwargs)
                    connection.commit()
                    print(f"[LOG] Transition Commited @:{time_stamp}")
                    return result
                except Exception as e:
                    connection.rollback()
                    print(f"[ERROR] Attempt {attempt}: Rolled back at {time_stamp} due to: {e}")
                    if attempt < retries:
                        print(f"[RETRY] Retrying in {delay}s...")
                        time.sleep(delay)
                    else:
                        print(f"[FAILURE] All {retries} attempts failed.")
                        raise
                time.sleep(delay)
        return wrapers
    return decorator


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
        connection = sqlite3.connect('users.db')
        try:
            return func(connection, *args, **kwargs)
        finally:
            connection.close()
    return wrapper


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)