#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ function that replaces all occurrences of an element by another
            in a new list."""
    new_list = []

    for nums in my_list:
        if search == nums:
            new_list.append(replace)
        else:
            new_list.append(nums)
    return new_list
