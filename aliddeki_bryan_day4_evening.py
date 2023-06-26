"""Day4 Monday 26th June 2023
    Evening session
"""

# importing square root and factorial from module math


# def greet(greeting):
"""greeting method"""
# print(greeting)


# greet("Hello lecturer. I look forward to the lecture")
# print("---------------------")


# Python Modules
# Simple calc


# def add(s, w):
"""add method"""
# return s + w


# def product(s, w):
"""multiply method"""
# return s * w


# import aliddeki_bryan_day4_evening

# print(aliddeki_bryan_day4_evening.product(8, 4))

# make sure they are in the same folder

# input and output in python


name = str(input("Enter your name: "))
age = int(input("ENter your age: "))


def check_age(name, age):
    """method to check age"""
    if age > 18:
        print(f"{name}, you are old enough to access this site haha")
    else:
        print(f"{name} you're still to young to continue to this site")


check_age(name, age)


s, r, w = map(int, input("Enter the values: ").split())
print("The values are: ", end=" ")
print(s, r, w)

my_list = [1, 2, 3, 5]
i = 0
for item in my_list:
    var = input(f"Enter new value for {item}:")
    my_list[i] = var
    i += 1
print(my_list)
