#!/usr/bin/python3
"""
Implements lazy pagination from the user_data table using a generator.
"""


import os
from dotenv import load_dotenv
import mysql.connector


# Load environment variables from .env file
load_dotenv()

# Access the variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def connect_db(include_database=True):
    """
    Connects to the MySQL server (optionally includes the database).
    """
    try:
        config = {
            "host": DB_HOST,
            "user": DB_USER,
            "password": DB_PASSWORD,
        }
        if include_database:
            config["database"] = DB_NAME

        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            msg = (
                f"Connected to MySQL database {DB_NAME}"
                if include_database else
                "Connected to MySQL server"
            )
            # print(msg)
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return None


def connect_to_prodev():
    """
    connects the the ALX_prodev database in MYSQL
    """
    temp_conn = connect_db(include_database=False)
    if temp_conn:
        # create_database(temp_conn)
        temp_conn.close()
        return connect_db(include_database=True)
    else:
        print("Failed to connect to MySQL server.")
        return None


def stream_user_ages():
    """
    a memory-efficient aggregate function i.e average age for a large dataset
    that yields user ages one by one.
    Use the generator in a different function to calculate the average age,
    without loading the entire dataset into memory
    Your script should print Average age of users: average age
    You must use no more than two loops in your script
    You are not allowed to use the SQL AVERAGE
    """
    connection = connect_to_prodev()
    if not connection:
        return

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        # print(row['age'])  # Print each age
        yield row['age']

    cursor.close()
    connection.close()


if __name__ == "__main__":
    total = 0
    count = 0
    for age in stream_user_ages():  # ✅ 1st and only loop
        total += float(age)
        count += 1

    if count > 0:
        print("Average age of users: {:.2f}".format(total / count))
    else:
        print("No user data found.")
