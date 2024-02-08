#!/usr/bin/python3
# base.py
"""
Module containing the Base class
"""


class Base:
    """ base class for alll obects in the project """

    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for the Base class """

        # If id is provided, use it, otherwise, increment
        # and use __nb_objects
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
