#!/usr/bin/python3

# 3-is_kind_of_class.py

""" function to check a class """


def is_kind_of_class(obj, a_class):
    """
    Return: True if the object is an instance of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
