#!/usr/bin/python3
"""
This script connects to a MySQL database,
creates a database named ALX_prodev if it does not exist,
creates a table named user_data with specified fields,
and inserts data into the table.
"""


import os
import csv
from dotenv import load_dotenv
import mysql.connector
import uuid


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
            print(msg)
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
        create_database(temp_conn)
        temp_conn.close()
        return connect_db(include_database=True)
    else:
        print("Failed to connect to MySQL server.")
        return None


def create_database(connection):
    """
    creates the database ALX_prodev if it does not exist
    """
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")


def create_table(connection):
    """
    creates a table user_data if it does not exists with the required fields
    """
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE
                user_data (
                    user_id CHAR(36) PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL UNIQUE,
                    age DECIMAL NOT NULL)
        """)
        connection.commit()
        print("Table user_data created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        cursor.close()


def insert_data(connection, data):
    """
    inserts data in the database if it does not exist
    """
    cursor = connection.cursor()
    try:
        cursor.execute("""
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name=VALUES(name), age=VALUES(age)
        """, data)
        connection.commit()
        print("Data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    finally:
        cursor.close()


def stream_csv_data(filepath):
    """
    Generator that yields validated rows from CSV one by one.
    Assumes CSV has no user_id column.
    """
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header

        for i, row in enumerate(reader, start=2):
            if len(row) != 3:
                print(f"Skipping line {i}: Invalid column count → {row}")
                continue

            name, email, age = row

            if not name.strip() or not email.strip() or not age.strip():
                print(f"Skipping line {i}: Missing fields → {row}")
                continue

            user_id = str(uuid.uuid4())
            yield (user_id, name.strip(), email.strip(), age.strip())


if __name__ == "__main__":
    conn = connect_to_prodev()
    if conn:
        create_table(conn)

        csv_file = "user_data.csv"

        for row in stream_csv_data(csv_file):
            insert_data(conn, row)

        conn.close()
        print("Connection closed.")
