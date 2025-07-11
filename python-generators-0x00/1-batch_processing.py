#!/usr/bin/env python3
"""
generator to fetch and process data in batches from the users database
"""


from dotenv import load_dotenv
import mysql.connector
import os


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def stream_users_in_batches(batch_size):
    """
    function that fetches rows in batches
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield from batch
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def batch_processing(batch_size):
    """
    function that processes each batch
    to filter users over the age of 25
    """
    for row in stream_users_in_batches(batch_size):
        if float(row.get('age', 0)) > 25:
            # print(f"User ID: {row['user_id']},
            # Name: {row['name']},
            # Email: {row['email']},
            # Age: {row['age']}")
            print(row)


if __name__ == "__main__":
    # Optional: demo call
    # batch_processing(50)
    pass
