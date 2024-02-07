#!/usr/bin/python3
# Rosita J Uqueio

"""Add all args to Python list & save them to a file."""
import sys
import json
from os.path import exists


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file."""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Load an object from a JSON file."""
    if exists(filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            return json.load(file)
    return []


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
