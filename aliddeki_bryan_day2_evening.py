#Exercise1: use the values () method to return a list of all values in the dictionary
student_marks = {
    "Jonah": 90,
    "Kirabo": 85,
    "Ali": 73,
    "Moses": 61,
    "Hadijjah": 43,
    "Simon": 80
}

print("The values of the student_marks are" ,student_marks.values())

#Exercise2: to check if a key exists in a dictionary
print("--------------------------------------------")
key = input("Enter a key to check if it exists in the dictionary: ")

key = str(key)
if key in student_marks:
    print("The key exists in the dictionary")
else:
    print("The key does not exist in the dictionary")
    exit()
print("--------------------------------------------")
#Exercise3: give an example on how to change dictionary items, how to update
update_value_key = input("Enter the student name to update: ")

update_value_mark = input("Enter the new mark: ")

update_value_key = str(update_value_key)
update_value_mark = int(update_value_mark)
if key in student_marks:
    student_marks[update_value_key] = update_value_mark
    print("Student mark has been updated. Here is the new dictionary: ", student_marks)
else:
    print("The key is not assigned to any value in the dictionary. Please try again")
print("--------------------------------------------")
#Exercise4: give an example on how to add dictionary items
add_value_key = input("Enter the student name to add: ")
add_value_mark = input("Enter the student mark to add: ")

add_value_key = str(add_value_key)
add_value_mark = int(add_value_mark)

student_marks.update({add_value_key: add_value_mark})
print("New student has been added. Here is the new dictionary: ", student_marks)
#Exercise5: give an example on how you can loop through a dictionary and also how to nest dictionaries within dictionaries

#looping through dictionaries
print("--------------------------------------------")
for key, value in student_marks.items():
    if(value > 80):
        print(key, "has an A")
    elif(value > 70):
        print(key, "has a B")
    elif(value > 60):
        print(key, "has a C")
    elif(value > 50):
        print(key, "has a D")
    elif(value > 40):
       print(key, "has an E")
    else:
        print("You failed")

#nesting dictionaries within dictionaries
print("--------------------------------------------")
student_marks = {"Jonah": {"Maths": 90, "English": 80, "Science": 70},
                 "Kirabo": {"Maths": 85, "English": 75, "Science": 65},
                    "Ali": {"Maths": 73, "English": 63, "Science": 53},
                    "Moses": {"Maths": 61, "English": 51, "Science": 41},
                    "Hadijjah": {"Maths": 43, "English": 33, "Science": 23},
                    "Simon": {"Maths": 80, "English": 70, "Science": 60}
                    }

for key, value in student_marks.items():
    for subject, subj_score in student_marks[key].items():
        if subject == "Maths":
            print("In Maths,", key, "has a score of: ", student_marks[key]["Maths"])
        elif subject == "English":
            print("In English,", key, "has a score of: ", student_marks[key]["English"])
        else:
            print("In Science,", key, "has a score of: ", student_marks[key]["Science"])

print("--------------------------------------------")


#STRINGS AND STRING MANIPULATION IN PYTHON

#Exercise1: use the len() function to determine the length of your string
name = "Aliddeki Bryan"
print("The length of the string is: ", len(name))
print("--------------------------------------------")

#Exercise2: Give an example of using a for loop in a string
for letter in name:
    print(letter)
print("--------------------------------------------")

#Exercise3: Give an example of slicing a string
print(name[0:8]) #prints the first 8 characters of the string

print(name[9:15:2]) #prints the characters from index 9 to 15, skipping every 2nd character

print("--------------------------------------------")

#Exercise: Use a condition to show how to use booleans

greeting = input('Enter a greeting whether you are  "FINE" or "NOT FINE": ')
greeting = str.upper(greeting)

if greeting == "FINE":
    print("I am glad you are fine")
elif greeting == "NOT FINE":
    print("I am sorry you are not fine")
else:
    print("Please enter a valid response")