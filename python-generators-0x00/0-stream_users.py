#!/usr/bin/python3
"""
This script connects to a MySQL database,
using a database named ALX_prodev,
and streams user data from the user_data table using a generator.
"""

from contextlib import closing
from dotenv import load_dotenv
import mysql.connector
import os
import sys


# Load environment variables from .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def stream_users():
    """
    Generator that fetches rows from user_data table one by one.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            print(f"Connected to MySQL database {DB_NAME}")
        else:
            print("Failed to connect to MySQL database")
            return

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row

        # Close cursor and connection after finishing the generator
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


# ✅ Export the function when imported dynamically
if __name__ != "__main__":
    sys.modules[__name__] = stream_users
