# DAY 06
# Advanced topics in Python

"""
regular expressions
generators and expressions
decorators
context managers
multithreading and multiprocessing

"""

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


"""while i < 10:
    if i < 0:
        print("Factorial does not exist for negative numbers")
    elif i == 0:
        factorial = 1
    else:
        factorial = factorial * i
    print(f"Factorial of {i} is {factorial}")
    i += 1"""


def factorial():
    result = 1
    for i in range(1, 10):
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


# outer_decorator()
# Context Manager - is an object defining a temporary contect for a block of code
# Example 1
"""def open_file(filename):
    file = open(filename, "r")

    def __enter__():
        return file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        file.close()

        return __enter__, __exit__


with open_file("text.txt") as f:
    print(f.read())"""

# Example 2 - Demnonstrate a context manager
import time


class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        end_time = time.time()
        execution_time = end_time - self.start
        print(f"The time for this exection is {execution_time} seconds")


with Timer() as timer:
    time.sleep(5)
    print("This is the end of the execution")
