#Exerceise1: use  the len() with the tuple example
#declare phones tuple
phones = ("Samsung", "iPhone", "Techno")

#print length of phones tuple
print("The length of the phones tuple is", (len(phones)))

#Exercise2: accessing tuples 
print("The item in index 2 is", phones[2], "\n")
print("The item in index 1 is", phones[1], "\n")
print("The item in index 0 is", phones[0], "\n")


"""
The code below shows declaration and sets manipulation
for exercise 3
"""

#set declaration
studentNames = {"Simon", "George", "Bryan", "Janette", "Terry"}

#finding length of set
print("The length of the set is ", len(studentNames), "\n")

#accessing set items
#set elements are unordered hence no keys and are thus accessed by their values

for studentName in studentNames:
    print(studentName)
print("--------------------------")

#adding items to a set
studentNames.add("Elizabeth")
studentNames.add("Stella-Maris")

print("---------------------------------The new set of studentNames is---------------------------------")
for studentName in studentNames:
    print(studentName)
print("-------------------------------------------------------------------------------------------------")

#adding two items together
set = {1, 3, 5, 7}
for number in set:
    sum = 0
    sum = number + number
print(sum)
print("---------------------------")

#adding sets together
set_1 = {1, 3, 5, 7}
set_2 = {0, 2, 4, 6}

#updating set_1 with set_2 values
set_1.update(set_2)

#printing the new updated set_1
print("When we add set_1 with set_2, we get" , set_1)
