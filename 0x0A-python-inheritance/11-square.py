#!/usr/bin/python3
# 11-square.py

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A representantion of a Square """
    def __init__(self, size):
        """ Instantiation of the square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of a sqaure """
        return self.__size * self.__size

    def __str__(self):
        """ Represents the string representation of a square """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
