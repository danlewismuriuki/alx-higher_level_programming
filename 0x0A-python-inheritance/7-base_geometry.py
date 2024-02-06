#!/usr/bin/python3

# 6-base_geometry.py

""" a class BaseGeometry (based on 5-base_geometry.py) """


class BaseGeometry():
    """
    class defines area method
    raises: excpetion area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Function validates value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
