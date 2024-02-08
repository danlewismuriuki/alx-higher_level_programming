#!/usr/bin/python3

# 10-square.py
""" module 10-square.py """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Represents a square """

    def __init__(self, size):
        """ Initializes a new square.

        Args:
             size (int): The size of the new square.
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.size * self.size
