#!/usr/bin/python3
"""
Implements lazy pagination from the user_data table using a generator.
"""

seed = __import__('seed')


def paginate_users(page_size, offset):
    """
    Fetch a page of users from the database with the given offset.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    Generator that lazily paginates over the user_data table.
    Only one loop is used as required.
    """
    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        for row in rows:
            yield row
        offset += page_size