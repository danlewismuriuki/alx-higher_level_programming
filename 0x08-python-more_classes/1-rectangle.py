#!/usr/bin/python3

# 1-rectangle.py
""" Write a class Rectangle that defines a rectangle """


class Rectangle:
    """ This class defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Represents a rectangle """
        self.width = width
        self.height = height

        @property
        def width(self):
            """getter for the private instance attr width """
            return self.__width

        @width.setter
        def width(self, value):
            """ Setter for the private instance attr width """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ getter for the private instance attr height """
            return self.__height

        @height.setter
        def height(self, value):
            """ Setter for the private instance attr height """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
