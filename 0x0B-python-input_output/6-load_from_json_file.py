#!/usr/bin/python3

# 6-load_from_json_file.py
""" a function that creates an Object from a “JSON file”: """
import json


def load_from_json_file(filename):
    """ method to read json file then convert to object file"""
    with open(filename, "r") as jsonfile:
        return json.load(jsonfile)
