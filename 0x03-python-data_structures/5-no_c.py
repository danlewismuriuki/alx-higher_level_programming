#!/usr/bin/env python3

def no_c(my_string):
    """prints all chars without the the removed chars"""
    new_string = ""

    for char in my_string:
        if char.lower() == "c":
            continue

        new_string += char

    return new_string
