#!/usr/bin/python3
# base.py
"""
Module containing the Base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
            # creates ajsn file dynamically
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:
            json_string = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
            )
            f.write(json_string)
