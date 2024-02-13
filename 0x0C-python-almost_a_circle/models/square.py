#!/usr/bin/python3
""" Defines the area of a square """
from .rectangle import Rectangle
"""
Rectangle Module

This module defines the Rectangle class, which represents rectangles.
It inherits from the Base class and adds functionality specific to rectangles,
such as width, height, and position.

Attributes:
    Rectangle: A class representing rectangles.

    Functions:
    validate_integer: Validates if a value is an integer.
"""


class Square(Rectangle):
    """
    Represents a square, a special case of a rectangle where
    all sides are equal.
    Inherits from Rectangle class.

    Attributes:
        size (int): The size of the square (equal to width and height).
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): The unique identifier of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.
        Args:
        size (int): The size of the square.
        x (int, optional): The x-coordinate of the top-left corner.
                            Defaults to 0.
        y (int, optional): The y-coordinate of the top-left corner.
                            Defaults to 0.
        id (int, optional): The unique identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method that returns the size of the square.
        Returns:
        int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method that sets the size of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Representation of reader friendly string of a class obj
        Returns a human-readable representation of the Square object.
        Returns:
            str: A string containing information about the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square object.

        Args:
            *args: Positional arguments (id, size, x, y).
            **kwargs: Keyword arguments (id, size, x, y).
        """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) >= 2 else self.size
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y

        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """
        Converts the Square object to a dictionary.

        Returns:
            dict: A dictionary containing the attributes of the Square object.
        """
        myDict = dict(id=self.id, size=self.size, x=self.x, y=self.y)
        return myDict
