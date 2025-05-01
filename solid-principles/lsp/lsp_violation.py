# Objects of a superclass should be replaceable with objects of its subclasses
# without affecting the correctness of the program.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

# Violates LSP because it modifies behavior of Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width  # Forces both width and height to be equal

    def set_height(self, height):
        self.height = height
        self.width = height  # Forces both width and height to be equal

# Function that expects a Rectangle but fails with Square
def process_shape(rectangle: Rectangle):
    rectangle.set_width(10)
    rectangle.set_height(5)
    print(f"Expected area: 10 * 5 = 50, Got: {rectangle.area()}")

# Usage
rect = Rectangle(2, 3)
square = Square(4)

process_shape(rect)    # Works correctly
process_shape(square)  # Violates LSP: Expected 50, but gets 25!
