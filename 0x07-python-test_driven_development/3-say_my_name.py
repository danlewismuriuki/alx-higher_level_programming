#!/usr/bin/python3
"""
This function prints first and lastname
"""
# 3-say_my_name.py


def say_my_name(first_name, last_name=""):
    """ Prints the first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name DEfaults to ""

    Raises:
        TypeError: If the first_name or last_name is not a string

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
