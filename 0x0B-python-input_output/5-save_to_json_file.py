#!/usr/bin/python3

# 5-save_to_json_file.py
"""
function that writes an Object to a text file,
    using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        jsong_string = json.dumps(my_obj)
        return f.write(json_string)
