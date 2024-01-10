#!/usr/bin/python3

def uniq_add(my_list=[]):
    """a function that adds all unique integers in a list
        (only once for each integer)."""
    uniq_set = set(my_list)
    return sum(uniq_set)
