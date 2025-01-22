import math

class Shape:
    """
    Base class representing a general shape.
    """
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        This method should be overridden in derived classes.
        """
        raise NotImplementedError("The 'area' method must be defined in subclasses.")

class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    """
    def __init__(self, length, width):
        """
        Initialize a rectangle with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle.
        Formula: length * width
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle.
    """
    def __init__(self, radius):
        """
        Initialize a circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        Formula: π * radius^2
        """
        return math.pi * self.radius**2
