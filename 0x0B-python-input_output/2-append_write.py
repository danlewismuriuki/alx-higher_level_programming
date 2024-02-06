#!/usr/bin/python3

# 2-append_write.py
""" a function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ Appends a string to a filename txt file """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
