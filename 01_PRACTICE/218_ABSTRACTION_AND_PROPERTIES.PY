from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    @property
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    @property
    def area(self):
        return 3.14 * self.r ** 2

# Usage
r = Rectangle(10, 5)
c = Circle(7)
print("Rectangle Area:", r.area)
print("Circle Area:", c.area)
