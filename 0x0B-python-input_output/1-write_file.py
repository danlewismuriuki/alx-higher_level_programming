#!/usr/bin/python3

# 1-write_file.py
""" Defining a file writing method """


def write_file(filename="", text=""):
    """ write a string to a text filename """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
