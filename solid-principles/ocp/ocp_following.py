from abc import ABC, abstractmethod
import math

# Base class for shapes (Open for extension, Closed for modification)
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

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Shape Calculator (Does not need modification when adding new shapes)
class ShapeCalculator:
    @staticmethod
    def calculate_area(shape: Shape):
        return shape.area()

# Usage
calculator = ShapeCalculator()
rect = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(3, 4, 5)

print(f"Rectangle Area: {calculator.calculate_area(rect)}")
print(f"Circle Area: {calculator.calculate_area(circle)}")
print(f"Triangle Area: {calculator.calculate_area(triangle)}")


