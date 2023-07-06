import time
import threading
import multiprocessing
import sqlite3


# Regular Expressions
"""
summary of regular expressions
\d - matches any digit
\b - matches any word boundary
\w - matches any alphanumeric character
\s - matches any whitespace character
re.search - searches a string for a match
re.match - matches a string at the beginning
re.findall - returns a list of all matches
re.sub - replaces one or many matches
"""
import re

match = re.search(r"\b\w+\b", "Python is fun")
print(f"match.group(): {match.group()}")

# Validate user input using regex
name = input("Please enter your name: ")
if re.match(r"^[A-Za-z]*$", name):
    print("Valid name")
else:
    print("Invalid name")

email = input("Please enter your email: ")
if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
    print("Valid email")
else:
    print("Invalid email")


# Generators and Iterators
# Print factorial of the first 10 numbers
def factorial():
    result = 1
    for i in range(1, 11):
        result *= i
        yield result


factorial_generator = factorial()
for value in factorial_generator:
    print(value)


# Decorators
def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()

    return inner


@my_decorator
def outer_decorator():
    print("This is the outer decorator")


outer_decorator()


# Context Manager - is an object defining a temporary context for a block of code
# context managers are basically used for managing resources in python eg help in closing a file


# Example 2 - Demonstrate a context manager
class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, traceback):
        end_time = time.time()
        execution_time = end_time - self.start
        print(f"The time for this execution is {execution_time} seconds")


with Timer() as timed:
    time.sleep(5)
    print("This is the end of the execution")


# Multithreading and Multiprocessing
# These are techniques that can be used to improve the performance of a Python program
# Multithreading - technique where multiple threads are created within a single process
# Multiprocessing - technique where multiple processes are created to execute segments of a program


# Example 1 - Multithreading
def task(task_name):
    """Creating task"""
    print(f"{task_name} is running")


# Create multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()


# Example 2 - Multiprocessing
def process_task(process_name):
    """Creating process"""
    print(f"{process_name} is running")


if __name__ == "__main__":
    # Create multiple processes
    pool = multiprocessing.Pool(processes=5)

    # Submit tasks to the pool
    for i in range(5):
        pool.apply_async(process_task, args=(f"Process {i}",))

    # Close the pool and wait for the work to finish
    pool.close()
    pool.join()


# 1. Create a context manager that allows us to open a file and write to it.
class FileHandler:
    """Context manager class for file handling"""

    def __init__(self, filename, mode):
        """Constructor"""
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with FileHandler("test.txt", "w") as f:
    f.write("Hello World")

print(f.closed)


# 2. Shows a context manager for managing a database connection.
class DatabaseConnection:
    """Context manager class for database connection"""

    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, traceback):
        self.conn.close()


with DatabaseConnection("test.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
    )
    cursor.execute("INSERT INTO test (name, age) VALUES (?, ?)", ("John", 25))
    cursor.execute("INSERT INTO test (name, age) VALUES (?, ?)", ("Jane", 30))
    cursor.execute("SELECT * FROM test")
    print(cursor.fetchall())


# 3. Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time


def timer(seconds):
    """Function to print the current time"""
    for _ in range(seconds):
        print(time.ctime())
        time.sleep(1)


def multithreading():
    """Function to run the timer function for 5 and 10 seconds"""
    thread1 = threading.Thread(target=timer, args=(5,))
    thread2 = threading.Thread(target=timer, args=(10,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


def multiProcess():
    """Function to run the timer function for 5 and 10 seconds"""
    process1 = multiprocessing.Process(target=timer, args=(5,))
    process2 = multiprocessing.Process(target=timer, args=(10,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()


if __name__ == "__main__":
    multithreading()
    multiProcess()
