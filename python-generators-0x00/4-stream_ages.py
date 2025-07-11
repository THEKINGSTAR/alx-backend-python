#!/usr/bin/python3
"""
Implements lazy pagination from the user_data table using a generator.
"""

data_base = __import__('seed').connect_to_prodev


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
    connection = data_base()
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
