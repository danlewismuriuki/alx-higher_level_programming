#!/usr/bin/python3

# 0-add_integer.py
""" Module has a function that adds two numbers together """


def add_integer(a, b=98):
    """ Adds two numbers together """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    else:
        return a + b
