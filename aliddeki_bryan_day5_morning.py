import tkinter as tk
from tkinter import simpledialog


# Demonstrating Inheritence
"""class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
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
        my_car.honk()"""


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


"""class Shape:
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
print("Area of rectangle: ", my_rectangle.calculate_area(12, 3))"""


# Abstraction

"""from abc import ABC, abstractmethod


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
"""
# Calculating the areas
"""print("Area of the circle:", circle.area())  # Output: Area of the circle: 78.5
print("Area of the rectangle:", rectangle.area())"""  # Output: Area of the rectangle: 24


# Demonstrate abstraction using calculating area of a circle and rectangle

# Create a receipt printing program with a GUI interface, a more advanced detail earns you more points

# Receipt printing program


class MainApplication(tk.Tk):
    """main application class"""

    market_items = {
        "sugar": {"qty": 20, "unit": "kg", "u_price": 5000},
        "salt": {"qty": 50, "unit": "bag", "u_price": 1000},
        "kakira_sugar": {"qty": 30, "unit": "kg", "u_price": 6000},
        "rice": {"qty": 80, "unit": "kg", "u_price": 4800},
        "basmat_rice": {"qty": 40, "unit": "kg", "u_price": 10000},
        "beans": {"qty": 60, "unit": "kg", "u_price": 3000},
        "picfare_books_96_small": {"qty": 100, "unit": "book", "u_price": 1000},
        "picfare_books_96_big": {"qty": 5, "unit": "book", "u_price": 3000},
        "pen": {"qty": 20, "unit": "pen", "u_price": 500},
        "pencil": {"qty": 20, "unit": "pencil", "u_price": 200},
        "eraser": {"qty": 15, "unit": "eraser", "u_price": 100},
        "picfare_ruler": {"qty": 30, "unit": "ruler", "u_price": 1000},
        "nike_air_shoes": {"qty": 10, "unit": "pair", "u_price": 80000},
        "t_shirt_polo": {"qty": 20, "unit": "piece", "u_price": 40000},
    }

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("700x800")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Create multiple frames/screens
        for F in (Frame1, Frame2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Frame1)

    def show_frame(self, frame_class):
        """show frame method"""
        frame = self.frames[frame_class]
        frame.tkraise()


class Frame1(tk.Frame):
    """frame 1 class"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.added_items = {}  # Initialize added_items as an empty dictionary

        label1 = tk.Label(
            self,
            text="---------------------------ROYALE SUPERMARKET---------------------------------\n---------------------------------Enter Customer Purchases---------------------------------",
            font=("Arial", 18),
            padx=5,
            pady=5,
        )
        list_box = tk.Listbox(self, width=40)
        i = 0
        for item in MainApplication.market_items:
            list_box.insert(i, item)
            i += 1

        added_items_view = tk.Text(self, width=40, height=20)

        button = tk.Button(
            self, text="Print Receipt", command=lambda: self.go_to_frame2()
        )

        label1.pack(side=tk.TOP, pady=10)
        list_box.pack(pady=10)
        added_items_view.pack(pady=10)
        button.pack(pady=10)

        self.added_items_view = (
            added_items_view  # Store the reference to the text widget
        )

        # method to handle adding of items to receipt
        def handle_selection(event):
            selected_item = list_box.get(list_box.curselection())
            quantity = simpledialog.askinteger(
                "Enter Quantity", f"Enter the quantity for {selected_item}"
            )
            if quantity:
                self.added_items[selected_item] = {
                    "quantity": quantity,
                    "unit_price": MainApplication.market_items[selected_item][
                        "u_price"
                    ],
                }
                added_items_view.insert(
                    tk.END, f"{selected_item} - Quantity: {quantity}\n"
                )

        # Bind the function to the ListboxSelect event
        list_box.bind("<<ListboxSelect>>", handle_selection)

    def go_to_frame2(self):
        """switch to frame 2"""
        self.controller.frames[Frame2].update_items(self.added_items)
        self.controller.show_frame(Frame2)


class Frame2(tk.Frame):
    """frame 2 class"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.added_items = {}  # Initialize added_items as an empty dictionary

        label = tk.Label(
            self, text="-------Receipt-------", font=("Arial", 18), pady=10
        )
        label.pack(pady=10)

        self.items_view = tk.Text(self, width=40, height=20)
        self.items_view.pack(pady=10)

        button = tk.Button(
            self,
            text="Go Back to Products",
            command=lambda: controller.show_frame(Frame1),
        )
        button.pack(pady=10)

    def update_items(self, added_items):
        """update items method"""
        self.added_items = (
            added_items  # Update added_items with the provided dictionary
        )
        self.display_items()

    def display_items(self):
        """display items method"""
        self.items_view.delete("1.0", tk.END)  # Clear the text widget
        total_price = 0
        overall_total = 0

        for item, details in self.added_items.items():
            quantity = details["quantity"]
            unit_price = details["unit_price"]
            total = quantity * unit_price

            self.items_view.insert(
                tk.END,
                f"Item: {item}\n"
                f"Quantity: {quantity}\n"
                f"Unit Price: {unit_price}\n"
                f"Total: {total}\n"
                "---\n",
            )

            total_price += total
            overall_total += total

        self.items_view.insert(tk.END, f"Overall Total: {overall_total}\n")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
