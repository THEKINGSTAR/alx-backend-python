#!/usr/bin/python3
"""
Using decorators to cache Database Queries (mandatory)
"""


from datetime import datetime
import functools
import time
import sqlite3 


query_cache = {}

"""your code goes here"""
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


def cache_query(func):
    """
    caches query results based on the SQL query string
    """
    @functools.wraps(func)
    def wrapper(connection, *args, **kwargs):
        query = kwargs.get("query")
        if query in query_cache:
            print(f"[CACHE HIT] Using cached result for: {query}")
            return query_cache[query]

        print(f"[CACHE MISS] Executing SQL: {query} at {datetime.now()}")
        result = func(connection, *args, **kwargs)
        query_cache[query] = result
        return result

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")