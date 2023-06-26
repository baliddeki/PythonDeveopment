"""Day4 Monday 26th June 2023

# Object Oriented Programming (OOP)

# Classes - blueprint for creating objects


class Car:
    #A class that represents a car.

    def __init__(self, car_make, car_model, car_year):
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year

    def start_engine(self):
        #Starts the car's engine.
        print("Engine has started")

    def stop_engine(self):
        #Stops the car's engine.
        print("Engine has stopped")


my_car = Car("Subaru", "Ranger", 2000)

print(my_car.car_model)
print(my_car.car_make)
print(my_car.car_year)
print(my_car.start_engine())
print(my_car.stop_engine())


# Simple Program to show student details
class Student:
    classs to show student details

    def __init__(self, name, regno):
        self.name = name
        self.regno = regno

    def display(self):
        print("Student name is: ", self.name)
        print("Student registration number is:", self.regno)


student_obj = Student("Bryan", "21/U/0663")
student_obj.display()


# Exercise
# Calculate the area and circumference of a circle


class AreaCircum:
    def __init__(self, radius, pie):
        self.radius = radius
        self.pie = pie

    def area(self):
        area = self.pie * self.radius * self.radius
        print("Area of the circle is", area)

    def circum(self):
        circum = 2 * self.pie * self.radius
        print("The circumference of the circle is", circum)


obj = AreaCircum(21, 3.14)
obj.area
obj.circum

class AreaPerim:
    def __init__(self, length, width):
        self.lengths = length
        self.width = width

    def area(self):
        area = self.length*self.width
        print("Area of the circle is", area)
    
    def perim(self):
        perim = 2*(self.length + self.width)
        print("Perimter of rectangle is", perim)
        
rect = AreaPerim
"""

"""bonus = 0.5 of salary 
employee1 salary =  150k
employee2 salary = """


class Employee:
    """Employee bonus constructor"""

    def __init__(self, salary):
        self.salary = salary

    def salary_calc(self):
        """Employee bonus"""
        bonus = 0.15 * self.salary
        print("Employee bonus is: ", bonus)


employee1 = Employee(15000)
employee2 = Employee(230000)
employee1.salary_calc()
employee2.salary_calc()
