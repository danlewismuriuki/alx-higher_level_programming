#!/usr/bin/python3

# 1-my_list.py
"""
This class sorts elements of an instance of a class
prints the sorted list
"""


class MyList(list):
    """ This class has a method which prints sorted elements """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
