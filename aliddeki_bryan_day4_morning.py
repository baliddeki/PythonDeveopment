# Day4 Monday 26th June 2023

# Object Oriented Programming (OOP)

# Classes - blueprint for creating objects


class Car:
    """A class that represents a car."""

    def __init__(self, car_make, car_model, car_year):
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year

    def start_engine(self):
        """Starts the car's engine."""
        print("Engine has started")

    def stop_engine(self):
        """Stops the car's engine."""
        print("Engine has stopped")


my_car = Car("Subaru", "Ranger", 2000)

print(my_car.car_model)
print(my_car.car_make)
print(my_car.car_year)
print(my_car.start_engine())
print(my_car.stop_engine())


# Simple Program to show student details
class Student:
    """classs to show student details"""

    def __init__(self, name, regno):
        self.name = name
        self.regno = regno

    def display(self):
        print("Student name is: ", self.name)
        print("Student registration number is:", self.regno)


student_obj = Student("Bryan", "21/U/0663")
student_obj.display()
