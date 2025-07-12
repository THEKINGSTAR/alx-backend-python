# ```Python Decorators```

<div margin="center" style="border: 1px solid #ccc; border-radius: 6px; padding: 16px;  margin-bottom: 20px;">

## **Project Description**

This project focuses on mastering Python decorators to enhance database operations in Python applications. Through hands-on tasks, learners will create custom decorators to log queries, handle connections, manage transactions, retry failed operations, and cache query results. The tasks are designed to simulate real-world challenges, providing learners with an in-depth understanding of Python’s capabilities for dynamic and reusable code in database management.


## **Learning Objectives**

**By completing these tasks, professional developers will:**

1. **Deepen their knowledge of Python decorators** and how they can be used to create reusable, efficient, and clean code.
1. **Enhance database management skills** by automating repetitive tasks like connection handling, logging, and caching.
1. **Implement robust transaction management techniques** to ensure data integrity and handle errors gracefully.
1. **Optimize database queries** by leveraging caching mechanisms to reduce redundant calls.
1. **Build resilience into database operations** by implementing retry mechanisms for transient errors.
1. **Apply best practices in database interaction** for scalable and maintainable Python applications.

## **Requirements**

- Python 3.8 or higher installed.
- SQLite3 database setup with a `users` table for testing.
- A working knowledge of Python decorators and database operations.
- Familiarity with Git and GitHub for project submission.
- Strong problem-solving skills and attention to detail.

## **Key Highlights**

1. **Task 0: Logging Database Queries**
    * Create a decorator to log all SQL queries executed by a function.
    * Learn to intercept function calls to enhance observability.

1. **Task 1: Handle Database Connections with a Decorator**
    * Automate database connection handling with a decorator.
    * Eliminate boilerplate code for opening and closing connections.

1. **Task 2: Transaction Management Decorator**
    * Implement a decorator to manage database transactions (commit/rollback).
    * Ensure robust error handling and data consistency.

1. **Task 3: Retry Database Queries**
    * Build a decorator to retry database operations on failure.
    * Introduce resilience against transient database issues.

1. **Task 4: Cache Database Queries**
    * Implement a decorator to cache query results.
    * Optimize performance by avoiding redundant database calls.



<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">


## **`0. Logging database Queries (mandatory)`**

**Objective:** create a decorator that logs database queries executed by any function

**Instructions:**

* Complete the code below by writing a decorator `log_queries` that logs the SQL query before executing it.

* Prototype: `def log_queries()`

```sh
import sqlite3
import functools

#### decorator to lof SQL queries

 """ YOUR CODE GOES HERE"""

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
```

#### **Repo**
- **GitHub repository**: `alx-backend-python`
- **Directory**: `python-decorators-0x01`
- **File**: `0-log_queries.py`

</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

## **`1. Handle Database Connections with a Decorator (mandatory)`**
**Objective:** create a decorator that automatically handles opening and closing database connections

**Instructions:**

Complete the script below by Implementing a decorator with_db_connection that opens a database connection, passes it to the function and closes it afterword

```sh
import sqlite3 
import functools

def with_db_connection(func):
    """ your code goes here""" 

@with_db_connection 
def get_user_by_id(conn, user_id): 
cursor = conn.cursor() 
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)
```

#### **Repo**
- **GitHub repository**: `alx-backend-python`
- **Directory**: `python-decorators-0x01`
- **File**: `1-with_db_connection.py`

</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

## **`2. Transaction Management Decorator (mandatory)`**

**Objective:** create a decorator that manages database transactions by automatically committing or rolling back changes

**Instructions:**

Complete the script below by writing a decorator transactional(func) that ensures a function running a database operation is wrapped inside a transaction.If the function raises an error, rollback; otherwise commit the transaction.


1. **Copy the with_db_connection created in the previous task into the script**
```sh
import sqlite3 
import functools

"""your code goes here"""

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
cursor = conn.cursor() 
cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
```

#### **Repo**
- **GitHub repository**: `alx-backend-python`
- **Directory**: `python-decorators-0x01`
- **File**: `2-transactional.py`

</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

## **`3. Using Decorators to retry database queries (mandatory)`**

**Objective:** create a decorator that retries database operations if they fail due to transient errors

**Instructions:**

Complete the script below by implementing a retry_on_failure(retries=3, delay=2) decorator that retries the function of a certain number of times if it raises an exception

```sh
import time
import sqlite3 
import functools

#### paste your with_db_decorator here

""" your code goes here"""

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
```

#### **Repo**
- **GitHub repository**: `alx-backend-python`
- **Directory**: `python-decorators-0x01`
- **File**: `3-retry_on_failure.py`

</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

## **`4. Using decorators to cache Database Queries (mandatory)`**

**Objective:** create a decorator that caches the results of a database queries inorder to avoid redundant calls

**Instructions:**

Complete the code below by implementing a decorator cache_query(func) that caches query results based on the SQL query string

```sh
import time
import sqlite3 
import functools


query_cache = {}

"""your code goes here"""

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
```

#### **Repo**
- **GitHub repository**: `alx-backend-python`
- **Directory**: `python-decorators-0x01`
- **File**: `4-cache_query.py`

</div>

<div style="border: 1px solid #ccc; border-radius: 6px; padding: 16px; margin: 20px auto; max-width: 800px;">

## **`5. Manual Review (mandatory)`**


#### **Repo**

- **GitHub repository**: `alx-backend-python`
- **Directory**: `python-decorators-0x01`

</div>
