#!/usr/bin/python3
# Dan Lewis

"""class Rectangle that defines a rectangle"""


class Rectangle:
    """Defines a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method to retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 == self.__height:
            return ""
        line = str(self.print_symbol) * self.__width
        rectangle_rows = [line] * self.__height
        return '\n'.join(rectangle_rows)

    def __repr__(self):
        """Returns a string representation of the rectangle to recreate it."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a farewell message when the instance is deleted."""
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns new Rectangle with width & height equal tos ize"""
        return (cls(size, size))
