# Classes should be open for extension, but closed for modification


import math

class ShapeCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height

        elif isinstance(shape, Circle):
            return math.pi * shape.radius ** 2

        elif isinstance(shape, Triangle):  # Every time a new shape is added, this class needs modification!
            s = (shape.a + shape.b + shape.c) / 2
            return math.sqrt(s * (s - shape.a) * (s - shape.b) * (s - shape.c))

        else:
            raise ValueError("Unknown shape")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

# Usage
calculator = ShapeCalculator()
rect = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(3, 4, 5)

print(f"Rectangle Area: {calculator.calculate_area(rect)}")
print(f"Circle Area: {calculator.calculate_area(circle)}")
print(f"Triangle Area: {calculator.calculate_area(triangle)}")
