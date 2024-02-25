#!/usr/bin/python3

"""
function that prints a square with the character #
"""


def print_square(size):
    """
    prints a square with the character #

    Args:
    size(size or float): Size will be a float or int

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    Return:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
