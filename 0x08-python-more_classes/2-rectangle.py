#!/usr/bin/python3
# 1-rectangle.py
"""Write a class Rectangle that defines a rectangle """


class Rectangle:
    """ class defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
           Width (int): The width of the rectangle.
           height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Getter for the private instance attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the private instance attribute height
        Args:
            value(int): The to set to the height
        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be >= 0")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ Getter for the private instance attribute height """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private instance attribute width
        Args:
            value(int): The to set to the width
        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be >= 0")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ Instance returns the area of the Rectangle """
        return (self.__width * self.__height)

        """ Instance returns the perimeter of the Rectangle """
    def perimeter(self):
        return (self.__width + self.__height) * 2
