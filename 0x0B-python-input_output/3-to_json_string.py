#!/usr/bin/python3

# 3-to_json_string.py
""" Defining a string to JSON function """
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object """
    json_string = json.dumps(my_obj)
    return json_string
