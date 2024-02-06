#!/usr/bin/python3

# 4-inherits_from.py

"""Defining a inheritance-checking function."""


def inherits_from(obj, a_class):
    """
    Return: True if the object is an instance of a class that
            inherited (directly or indirectly) from the specified class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
