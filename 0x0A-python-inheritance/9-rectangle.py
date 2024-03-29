#!/usr/bin/python3

# 9-rectangle.py
""" Module 9-rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle has inherited Basegeometry attr
    """
    def __init__(self, width, height):
        """ instatiation of the rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ calculates the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string representation of the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
