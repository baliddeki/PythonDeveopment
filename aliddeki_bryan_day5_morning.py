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


class Shape:
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
print("Perimeter of rectangle: ", my_rectangle.perimeter())
