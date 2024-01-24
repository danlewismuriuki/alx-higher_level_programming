#!/usr/bin/python3
""" class Square that defines a square by: (based on 4-square.py) """


class Square:
    """ Initialze an instance with size attribute """
    def __init__(self, size=0):
        self.size = size

    """ Getter Method with a private attribute size """

    @property
    def size(self):
        return self.__size

    """ Setter Method with a private attribute value
        args:
        value (int): value to be set
        raises:
            TypeError: if value is not int
                         TypeError("size must be an integer")

            ValueErro: if value is < 0  must be >= 0
                         ValueError("size must be >= 0")
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ Method to square the size """

    def area(self):
        return self.__size ** 2

    """
           Method to print #
           prints in stdout the square with the character #
    """

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
