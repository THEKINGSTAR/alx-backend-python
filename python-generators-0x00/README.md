# **`Python Generators`**

<div margin="center" style="border: 1px solid #ccc; border-radius: 6px; padding: 16px;  margin-bottom: 20px;">


## **`About the Project`**

This project introduces advanced usage of Python generators to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations. The tasks focus on leveraging Python’s yield keyword to implement generators that provide iterative access to data, promoting optimal resource utilization, and improving performance in data-driven applications.

## **Learning Objectives**

### **By completing this project, you will:**

1. **Master Python Generators:** Learn to create and utilize generators for iterative data processing, enabling memory-efficient operations.

1. **Handle Large Datasets:** Implement batch processing and lazy loading to work with extensive datasets without overloading memory.

1. **Simulate Real-world Scenarios:** Develop solutions to simulate live data updates and apply them to streaming contexts.

1. **Optimize Performance:** Use generators to calculate aggregate functions like averages on large datasets, minimizing memory consumption.

1. **Apply SQL Knowledge:** Use SQL queries to fetch data dynamically, integrating Python with databases for robust data management.

## **Requirements**

1. Proficiency in `Python 3.x`.
1. Understanding of yield and Python’s generator functions.
1. Familiarity with `SQL` and database operations (`MySQL` and `SQLite`).
1. Basic knowledge of database schema design and data seeding.
1. Ability to use `Git` and `GitHub` for version control and submission.




# **`Tasks`**

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

##`# **0. Getting started with python generators `(mandatory)`**

</div>

**Objective: create a generator that streams rows from an SQL database one by one.**

**Instructions:**

* Write a python script that seed.py:

    * Set up the MySQL database, `ALX_prodev` with the table user_data with the following fields:
    * `user_id(Primary Key, UUID, Indexed)`
    * `name (VARCHAR, NOT NULL)`
    * `email (VARCHAR, NOT NULL)`
    * `age (DECIMAL,NOT NULL)`
    * Populate the database with the sample data from this [user_data.csv](./user_data.csv)
        * **Prototypes:**
    * `def connect_db()`: - connects to the mysql database server
    * `def create_database(connection)`: - creates the database `ALX_prodev` if it does not exist
    * `def connect_to_prodev()` connects the the `ALX_prodev` database in MYSQL
    * `def create_table(connection)`:- creates a table `user_data` if it does not exists with the required fields
    * `def insert_data(connection, data)`:- inserts data in the database if it does not exist

```sh
faithokoth@ubuntu:python-generators-0x00 % cat 0-main.py
#!/usr/bin/python3

seed = __import__('seed')

connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print(f"connection successful")

    connection = seed.connect_to_prodev()

    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')
        cursor = connection.cursor()
        cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print(f"Database ALX_prodev is present ")
        cursor.execute(f"SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print(rows)
        cursor.close()

faithokoth@ubuntu:python-generators-0x00 % ./0-main.py
connection successful
Table user_data created successfully
Database ALX_prodev is present 
[('00234e50-34eb-4ce2-94ec-26e3fa749796', 'Dan Altenwerth Jr.', 'Molly59@gmail.com', 67), ('006bfede-724d-4cdd-a2a6-59700f40d0da', 'Glenda Wisozk', 'Miriam21@gmail.com', 119), ('006e1f7f-90c2-45ad-8c1d-1275d594cc88', 'Daniel Fahey IV', 'Delia.Lesch11@hotmail.com', 49), ('00af05c9-0a86-419e-8c2d-5fb7e899ae1c', 'Ronnie Bechtelar', 'Sandra19@yahoo.com', 22), ('00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4', 'Alma Bechtelar', 'Shelly_Balistreri22@hotmail.com', 102)]

faithokoth@h@ubuntu:python-generators-0x00 % 
```

## **Repo:**

- **GitHub repository:** `alx-backend-python`
- **Directory:** `python-generators-0x00`
- **File:** `seed.py`, `README.md`


</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">
<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

### **1. generator that streams rows from an SQL database `(mandatory)`**

</div>

**Objective: create a generator that streams rows from an SQL database one by one.**

### **Instructions:**

In 0-stream_users.py write a function that uses a generator to fetch rows one by one from the user_data table. You must use the Yield python generator


**Prototype:** def stream_users()

Your function should have no more than 1 loop

```sh
(venv)faithokoth@Faiths-MacBook-Pro python-generators-0x00 % cat 1-main.py 

#!/usr/bin/python3
from itertools import islice
stream_users = __import__('0-stream_users')

# iterate over the generator function and print only the first 6 rows

for user in islice(stream_users(), 6):
    print(user)

(venv) faithokoth@Faiths-MacBook-Pro python-generators-0x00 %./1-main.py

{'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}
{'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}
{'user_id': '006e1f7f-90c2-45ad-8c1d-1275d594cc88', 'name': 'Daniel Fahey IV', 'email': 'Delia.Lesch11@hotmail.com', 'age': 49}
{'user_id': '00af05c9-0a86-419e-8c2d-5fb7e899ae1c', 'name': 'Ronnie Bechtelar', 'email': 'Sandra19@yahoo.com', 'age': 22}
{'user_id': '00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4', 'name': 'Alma Bechtelar', 'email': 'Shelly_Balistreri22@hotmail.com', 'age': 102}
{'user_id': '01187f09-72be-4924-8a2d-150645dcadad', 'name': 'Jonathon Jones', 'email': 'Jody.Quigley-Ziemann33@yahoo.com', 'age': 116}

(venv) faithokoth@Faiths-MacBook-Pro python-generators-0x00 %
```

## **Repo:**

- **GitHub repository:** `alx-backend-python`
- **Directory:** `python-generators-0x00`
- **File:** `0-stream_users.py`


</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

### **2. Batch processing Large Data `(mandatory)`**

</div>

Objective: Create a generator to fetch and process data in batches from the users database

### **Instructions:**

Write a function stream_users_in_batches(batch_size) that fetches rows in batches

Write a function batch_processing() that processes each batch to filter users over the age of25`

You must use no more than 3 loops in your code. Your script must use the yield generator

**Prototypes:**

def stream_users_in_batches(batch_size)
def batch_processing(batch_size)

```sh
(venv) faithokoth@Faiths-MacBook-Pro python-generators-0x00 % cat 2-main.py                
#!/usr/bin/python3
import sys
processing = __import__('1-batch_processing')

##### print processed users in a batch of 50
try:
    processing.batch_processing(50)
except BrokenPipeError:
    sys.stderr.close()

(venv) faithokoth@Faiths-MacBook-Pro python-generators-0x00 % ./2-main.py | head -n 5 

{'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}

{'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}

{'user_id': '006e1f7f-90c2-45ad-8c1d-1275d594cc88', 'name': 'Daniel Fahey IV', 'email': 'Delia.Lesch11@hotmail.com', 'age': 49}

{'user_id': '00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4', 'name': 'Alma Bechtelar', 'email': 'Shelly_Balistreri22@hotmail.com', 'age': 102}

{'user_id': '01187f09-72be-4924-8a2d-150645dcadad', 'name': 'Jonathon Jones', 'email': 'Jody.Quigley-Ziemann33@yahoo.com', 'age': 116}

(venv) faithokoth@Faiths-MacBook-Pro python-generators-0x00 % 
```

## **Repo:**

- **GitHub repository:** `alx-backend-python`
- **Directory:** `python-generators-0x00`
- **File:** `1-batch_processing.py`

</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

### **3. Lazy loading Paginated Data `(mandatory)`**

</div>

Objective: Simulte fetching paginated data from the users database using a generator to lazily load each page

### **Instructions:**

Implement a generator function lazypaginate(pagesize) that implements the paginate_users(page_size, offset) that will only fetch the next page when needed at an offset of 0.

You must only use one loop
Include the paginate_users function in your code
You must use the yield generator

**Prototype:**

def lazy_paginate(page_size)

#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


```sh

(venv) faithokoth@Faiths-MacBook-Pro python-generators-0x00 % cat 3-main.py
#!/usr/bin/python3
import sys
lazy_paginator = __import__('2-lazy_paginate').lazy_pagination


try:
    for page in lazy_paginator(100):
        for user in page:
            print(user)

except BrokenPipeError:
    sys.stderr.close()
(venv) faithokoth@Faiths-MacBook-Pro python-generators-0x00  % python 3-main.py | head -n 7

{'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}

{'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}

{'user_id': '006e1f7f-90c2-45ad-8c1d-1275d594cc88', 'name': 'Daniel Fahey IV', 'email': 'Delia.Lesch11@hotmail.com', 'age': 49}

{'user_id': '00af05c9-0a86-419e-8c2d-5fb7e899ae1c', 'name': 'Ronnie Bechtelar', 'email': 'Sandra19@yahoo.com', 'age': 22}

{'user_id': '00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4', 'name': 'Alma Bechtelar', 'email': 'Shelly_Balistreri22@hotmail.com', 'age': 102}

{'user_id': '01187f09-72be-4924-8a2d-150645dcadad', 'name': 'Jonathon Jones', 'email': 'Jody.Quigley-Ziemann33@yahoo.com', 'age': 116}

{'user_id': '01ab6c5d-7ae2-4968-991a-d63e93d8d025', 'name': 'Forrest Heaney', 'email': 'Albert51@hotmail.com', 'age': 104}
(venv) faithokoth@Faiths-MacBook-Pro python-generators-0x00 %
```

## **Repo:**

- **GitHub repository:** `alx-backend-python`
- **Directory:** `python-generators-0x00`
- **File:** `2-lazy_paginate.py`

</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">
 <div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

### **4. Memory-Efficient Aggregation with Generators `(mandatory)`**

</div>

Objective: to use a generator to compute a memory-efficient aggregate function i.e average age for a large dataset

### **Instruction:**

Implement a generator stream_user_ages() that yields user ages one by one.

Use the generator in a different function to calculate the average age without loading the entire dataset into memory

Your script should print Average age of users: average age

You must use no more than two loops in your script

You are not allowed to use the SQL AVERAGE


## **Repo:**

- **GitHub repository:** `alx-backend-python`
- **Directory:** `python-generators-0x00`
- **File:** 4-stream_ages.py

</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">
 
<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

### **5. Manual Review `(mandatory)`**

</div>

## **Repo:**


- **GitHub repository:** `alx-backend-python`
- **Directory:** `python-generators-0x00`

</div>



Copyright © 2025 ALX, All rights reserved.
