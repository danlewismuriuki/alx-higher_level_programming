#!/usr/bin/python3

""" This is the  class Square that defines a square """


class Square:
    """ contains private instance attribute. """
    def __init__(self, size=0):
        """ Initializes the sqaure class with size attribute
            args:
               size (int) : The size of the square. DEfault is 0
            Raises:
                 TypeError: if not instance of int
                             return size must be an integer
                 ValueError: if size < 0 print exception
                             with the message size must be >= 0
    """
        self.size = size

    """ get method to get the size attribute """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """This is set the size of squares

            args:
                value (int) : size of the square

            raises:
                TypeError: if not instance of int
                              return size must be an integer
                ValueError: if size < 0 print exception with the message
                              size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        """ returns current square area """

    def area(self):
        """ public function or method to calculate the area """
        return self.__size ** 2
