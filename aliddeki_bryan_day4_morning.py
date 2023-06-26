"""Day4 Monday 26th June 2023

Object Oriented Programming (OOP)

Classes - blueprint for creating objects
"""

"""
1. inheritence
2. polymorphism
3. abstraction
"""


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

print("------------------------------------------------------------------")


# Simple Program to show student details
class Student:
    """classs to show student details"""

    def __init__(self, name, regno):
        self.name = name
        self.regno = regno

    def display(self):
        """moethod to display student details"""
        print("Student name is: ", self.name)
        print("Student registration number is:", self.regno)


student_obj = Student("Bryan", "21/U/0663")
student_obj.display()
print("----------------------------------------------------------")


# Exercise
# Calculate the area and circumference of a circle


class AreaCircum:
    """program to calculate area and circumference of a circle"""

    def __init__(self, radius, pie):
        self.radius = radius
        self.pie = pie

    def area(self):
        """method to calculate area of circle"""
        area = self.pie * self.radius * self.radius
        print("Area of the circle is", area)

    def circum(self):
        """method to calculate perimeter of circle"""
        circum = 2 * self.pie * self.radius
        print("The circumference of the circle is", circum)


obj = AreaCircum(21, 3.14)
obj.area()
obj.circum()
print("--------------------------------------------------")


# Program to print area and perimeter of a rectangle
class AreaPerim:
    """constructor"""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """method to calculate area of rectangle"""
        area = self.length * self.width
        print("Area of the circle is", area)

    def perim(self):
        """method to calculate perimeter of rectangle"""
        perim = 2 * (self.length + self.width)
        print("Perimter of rectangle is", perim)


rect = AreaPerim(20, 40)
rect.area()
rect.perim()
print("------------------------------------------------------------------")


# Program to calculate employee bonus


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
print("-------------------------------------------------------------")

# Encapsulation
# Key Goals of encapsulation

# 1. hide implementation details of an object
# 2. protect object from changes
# 3. protect object from external changes
# 4. code organization and modularity

# Example with a bank account


class BankAccount:
    """bank account constructor"""

    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        """deposit method"""
        self._balance += amount

    def withdraw(self, amount):
        """withdraw method"""
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        """get balance method"""
        return self._balance


my_account = BankAccount("3200100783", 200000)

print("Account number:", my_account._account_number)
print("Balance:", my_account._balance)
my_account.deposit(50000)
print("Balance:", my_account._balance)
my_account.withdraw(100000)
print("Balance:", my_account._balance)
print("---------------------------------------------")

# Exercise2: Convert temperature from degress Celcius to Fahrenheight


class Temperature:
    """program to convert from degree Celcus to Fahrenheight"""

    def __init__(self):
        self._temp = int(input("Enter the temperature to be converted: "))

    def convert(self):
        """method to convert celcius to fahrenheight"""
        fahren = (self._temp * (9 / 5)) + 32
        return fahren

    def get_fahren_temp(self):
        """method to return to new converted to temperature"""
        return self.convert()


tempObj = Temperature()
print(tempObj.get_fahren_temp())

print("-------------------------------------------------------------------------------")


# Assignment2: Show encapsulation with employee information to give a pay incrementation to give
# a pay incrementation (Salary with employee information to new_salary) eg from 850000 to 1000000


# Program to increase/decrease salary of employee
class EmployeeIncrement:
    """class constructor"""

    def __init__(self, employees):
        self.employees = employees
        print("The available employees current salaries are:")
        for key, value in employees.items():
            print(key, ":", value)
        self.employee_name = input(
            "Enter the name of employee to be increased salary: "
        )
        if self.employee_name in self.employees.keys():
            self.__salary = self.employees[self.employee_name]

        else:
            print("Employee not in the system. First register employee")

    def get_salary(self):
        """salary get method"""
        return self.__salary

    def set_salary(self, n_salary):
        """salary set method"""
        self.__salary = n_salary

    def change_salary(self):
        """method to change salary of employee"""

        # check if employee is in the system
        if self.employee_name in self.employees.keys():
            new_salary = input("Enter the new employee salary: ")
            print(self.employee_name, "new salary is", new_salary)

            # confirm salary change
            confirm = input("Type OK to confirm: ")
            confirm_to_upper = confirm.upper()
            confirm_stripped = confirm_to_upper.strip()

            # formatting confirmation input - capitalizing and removing white spaces
            if (confirm_stripped) == "OK":
                self.__salary = new_salary
                self.employees[self.employee_name] = new_salary
            else:
                print("Try again to change employee salary")
        else:
            print("Employee not in the system. First register employee")

    def print_new_salary(self):
        """method to print new salaries"""
        print("The available new employees current salaries are:")
        for key, value in self.employees.items():
            print(key, ":", value)


# dictionary of employees
employee = {
    "Aliddeki Bryan": 500000,
    "Nantume Stellah": 800000,
    "Nsereko Julius": 400000,
}

"""for key, value in employee.items():
    print(key, value)"""

empObj = EmployeeIncrement(employee)
empObj.change_salary()
empObj.print_new_salary()
