from abc import ABC, abstractmethod
import math

# Abstract base class using ABC module
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

# Concrete class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")

# Concrete class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        print(f"Drawing a Rectangle of size {self.width}x{self.height}")

# Concrete class Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print(f"Drawing a Triangle with base {self.base} and height {self.height}")

# Multiple inheritance: Colored shape
class ColoredShape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"Color: {self.color}")

# Combined class: ColoredCircle inherits from Circle and ColoredShape
class ColoredCircle(Circle, ColoredShape):
    def __init__(self, radius, color):
        Circle.__init__(self, radius)
        ColoredShape.__init__(self, color)

    def draw(self):
        super().draw()
        self.display_color()

# Duck typing example
class Printer:
    def print_shape(self, shape):
        print("Area:", shape.area())
        shape.draw()


# Driver code
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4),
    ColoredCircle(7, "blue")
]

printer = Printer()

for shape in shapes:
    print("\n--- Shape Info ---")
    printer.print_shape(shape)
