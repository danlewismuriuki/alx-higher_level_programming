#!/usr/bin/python3

# 1-my_list.py
"""
This class sorts elements of an instance of a class
prints the sorted list
"""


class MyList(list):
    """ This class has a method which prints sorted elements """
    def __init__(self):
        """ Initialize the  list object """
        super().__init__()

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
