#!/usr/bin/python3

# 4-from_json_string.py

"""a function that returns an object """
import json


def from_json_string(my_str):
    """Method to convert Json string to python data structure """
    py_data = json.loads(my_str)
    return py_data
