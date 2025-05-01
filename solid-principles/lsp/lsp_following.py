from abc import ABC, abstractmethod

# Base class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Function that works with any shape
def process_shape(shape: Shape):
    print(f"Area: {shape.area()}")

# Usage
rect = Rectangle(10, 5)
square = Square(4)

process_shape(rect)   # Output: 50
process_shape(square) # Output: 16
