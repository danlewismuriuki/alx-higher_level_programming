#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ class Instantiation """
    def __init__(self, size=0):
        """ Initializes the square class with a size attribute

        Args:
            size (int): Size of square. default is 0.

        Raises:
            TypeError: If size is not Int
            ValueError: If size is less that 0
    """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
