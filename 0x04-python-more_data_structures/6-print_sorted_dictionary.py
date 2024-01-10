#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.keys())

    for key in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(key, a_dictionary[key]))
