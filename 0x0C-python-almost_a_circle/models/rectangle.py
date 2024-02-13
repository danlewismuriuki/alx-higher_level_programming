#!/usr/bin/python3
""" Defines a rectangle class """
# Base = __import__("base").Base
from .base import Base

"""
Rectangle Module

This module defines the Rectangle class, which represents rectangles
It inherits from the Base class and adds functionality specific to rectangles,
such as width, height, and position.

Project Summary
    The project aims to provide a framework for handling geometric shapes,
    with a focus on rectangles. It provides a base class (Base)
        for common functionality and extends it with the Rectangles class.

Key Features:
    - Rectangle class for representation rectangles
    - Base class for shared functionality among geometric shapes
    - Support for setting and getting width, height, position,
        and unique identifier
"""


class Rectangle(Base):
    """ Represents a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left
            y (int, optional): The y-coordinate of the top-left corner
            id (int, optional): The unique identifier of
                the rectangle (default is none)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute

        Args:
           value (int): The new value for the width

        Raises:
            ValueError: If the value is not a positive integer
        """
        self.validate_integer("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for ther height atttribute

        Args:
            value (int): The new value for the height

        Raises:
            ValueError: If the value s not a positive integer
        """
        self.validate_integer("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the width attribute

        Returns:
            int: The x-coordinate of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for ther x atttribute

        Args:
            Value (int): The new value for the x-coordinate
        Raises:
            ValueError: if the value is not a non-negatie
        """
        self.validate_integer("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute

        Returns:
            int: The y-coordinate of the rectange
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the x atttribute

        Args:
            value (int): Th new value for the y-coordinate.

        Raises:
            ValueError: If the value is not a non-negative integer.
        """
        self.validate_integer("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def validate_integer(self, name, value):
        """ Validates if the value is an integer """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return (self.__height * self.__width)

    def display(self):
        """
        Prints the Rectangle instance with '#' characters
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle

        Returns:
            str: A string representation of the Rectangle
        """
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height
                )

    # def update(self, *args):
    #    attributes = ["id", "width", "height", "x", "y"]
    #    for i in range(min(len(args), len(attributes))):
    #       setattr(self, attributes[i], args[i])

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle object.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments

        Note:
            If both positional and keyword arguments are provided,
            the method prioritizes keyword arguments.

        Examples:
            rect = Rectangle(1, 2, 3, 4)
            rect.update(5, 6, 7, 8) Updates id, width, height, and x,
                respectively
            rect.update(width=10, height=20,) Updates width and height
        """
        if args:
            self.id = arg[0] if len(args) >= 1 else self.id
            self.width = arg[1] if len(args) >= 2 else self.width
            self.height = arg[2] if len(args) >= 2 else self.height

        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)

    def to_dictionary(self):
        """
        converts the Rectangle object to a ddictionary representation

        Returns:
            dict: A dictionary containing the attributes of the
                Rectangle object
        Example:
            rect = Rectangle(1, 2, 3, 4)
            rect_dict = rect.to_dictionary()
                #{
                'id': 1,
                'width':2,
                'height': 3,
                'x': 4,
                'y': 5
                }
        """
        """
        myDict = {
                id: "self.id",
                width: "self.width",
                height: "self.height",
                x: "self.x",
                y: "self.y"
                }
         """
        myDict = dict(
                x=self.x,
                y=self.y,
                id=self.id,
                height=self.height,
                width=self.width
        )
        return myDict
