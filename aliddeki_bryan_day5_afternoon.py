# Python File Handling
"""
Adavantages of file handling
1. versatility
2. flexibility
3. user-friendly
4. cross-platform

Disadvantages of file handling
1. error-prone (file permissions, file locks)
2. security issues
3. complexity
4. performance

"""

# open() function
# open() function is used to open a file and return a file object

# modes
# r - read mode
# w - write mode
# a - append mode
# r+ - read and write mode
# w+ - write and read mode
# a+ - append and read mode

file = open("aliddeki_bryan_day3_morning.py", "r")
for line in file:
    print(line)

# read file using with statement
with open("aliddeki_bryan_day3_morning.py") as file:
    data = file.read()

print(data)

# split lines while reading files
with open("aliddeki_bryan_day3_morning.py") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)


# Writing data to a file
file = open("text_file.txt", "w")
file.write("Hello World!")
file.write("\nThis is a new line")
file.close()

# showing overriding of text
file = open("text_file.txt", "w")
file.write("\nThis has overridden the previous text")
file.close()

# program demonstrating file handling and exception handling
import os


def create_file(file_name):
    try:
        file = open(file_name, "w+")
        file.close()
    except IOError:
        print("Error: File already exists")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("Error: File not found")


def append_file(file_name, text):
    try:
        file = open(file_name, "a+")
        file.write(text)
        file.close()
    except IOError:
        print("Error: File not found")


def read_file(file_name):
    try:
        file = open(file_name, "r")
        data = file.read()
        print(data)
        file.close()
    except IOError:
        print("Error: File not found")


file_name = input("Enter file name: ")
create_file(file_name)
delete_file(file_name)


# Exception Handling in Python
# Sample Program
emotion_dict = {
    1: "I guess something is wrong. Let's have a chat...may be it will make you feel better",
    2: "What is wrong?",
    3: "Not so bad. But you could be better",
    4: "This is slightly below average. Try listening to music",
    5: "This is average. You could be better",
    6: "This is above average. You are doing great",
    7: "This is great. Keep it up",
    8: "This is very great. You are doing very well",
    9: "This is excellent. You are doing excellent",
    10: "This is outstanding. You are outstanding",
}

feeling = input("Give a rating of your feeling in the range 1 to 10: ")

try:
    feeling = int(feeling)
    if feeling > 5:
        print("Number not in range.")
    elif 1 < feeling < 5:
        print(emotion_dict[feeling])
        shared_feeling = input(
            "You can share with me what you're feeling or talk to a friend? "
        )
        if shared_feeling != "":
            print(
                "Thank you for sharing with me. Let me connect you to a pyschologist for more help"
            )
            print(shared_feeling)
        else:
            exit()
    else:
        print(emotion_dict[feeling])
except ValueError:
    print("Please enter a number in the range 1 to 5.")
    exit()
finally:
    print("Thank you for your participation.")
