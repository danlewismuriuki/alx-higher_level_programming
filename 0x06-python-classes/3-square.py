#!/usr/bin/python3

""" class Square that defines a square by: (based on 2-square.py) """


class Square:
    """ Initialize class square with a private instance attribute
    Args:
    size (int): Default is zero. Is of type int
    Raises:
    ValueError: If not int gives message of size must be an integer
    TypeError: If not int size must be >= 0

    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = size

    """ Returns area of the square """

    def area(self):
        return (self.__size * self.__size)
