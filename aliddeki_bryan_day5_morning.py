# Demonstrating Inheritence
"""class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def display _info(self):
        print("Brand: ", self.brand)
        print("Color: ", self.color)
    
    def move(self):
        print("Moving the vehicle.")
    
    class Car(Vehicle):
        def __init__(self, brand, color, num_wheels):
            self.num_wheels = num_wheels
            super().__init__(brand, color)
        
        def display_info(self):
            super().display_info()
            print("Number of wheels: ", self.num_wheels)
        
        def honk(self):
            print("Honk honk!")
        
        my_car = Car("Toyota", "Red", 4)
        my_car.display_info()
        my_car.move()
        my_car.honk()
"""

# Demonstrate using inhertence to calculate the area and perimter of a circle and rectangle


"""class Shape:
    def __init__(self, length):
        self.length = length


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = self.length

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


my_circle = Circle(5)
print("Area of circle: ", my_circle.area())
print("Perimeter of circle: ", my_circle.perimeter())

my_rectangle = Rectangle(5, 10)
print("Area of rectangle: ", my_rectangle.area())
print("Perimeter of rectangle: ", my_rectangle.perimeter())"""


# Multiple Inheritence
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

    def display_info(self):
        print(f"Name: {self.name}")


class Flyable:
    def fly(self):
        print(f"{self.name} is flying...")


class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        super().display_info()
        print(f"Species: {self.species}")
        print(f"Name: {self.name}")


my_bird = Bird("Pigeon", "bird")
my_bird.display_info()
my_bird.eat()
my_bird.fly()


class Animal:
    def make_sound(self):
        print("Animal is making a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")


class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing")


def make_animal_sound(animal):
    animal.make_sound()


# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

# Method overloading
# Method overloading is no directly supported in Python


class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def calculate_area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def calculate_area(self, length, width):
        return length * width


my_circle = Circle()
my_rectangle = Rectangle()

print("Area of circle: ", my_circle.calculate_area(5))
print("Area of rectangle: ", my_rectangle.calculate_area(12, 3))


# Abstraction

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculating the areas
print("Area of the circle:", circle.area())  # Output: Area of the circle: 78.5
print("Area of the rectangle:", rectangle.area())  # Output: Area of the rectangle: 24


# Demonstrate abstraction using calculating area of a circle and rectangle

# Create a receipt printing program with a GUI interface, a more advanced detail earns you more points

# Receipt printing program
