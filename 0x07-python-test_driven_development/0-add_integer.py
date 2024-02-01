#!/usr/bin/python3

# 0-add_integer.py
""" Module has a function that adds two numbers together """


def add_integer(a, b=98):
    """ Adds two numbers together
    Args:
        a (int or float): The first num
        b (int or float): The second num
                          Default - 98
    Returns:
        int: The sum of the two nums
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
