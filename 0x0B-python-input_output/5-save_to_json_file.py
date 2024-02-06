#!/usr/bin/python3

# 5-save_to_json_file.py
"""
function that writes an Object to a text file,
    using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a file """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
