#!/usr/bin/python3

# 1-write_file.py

def write_file(filename="", text=""):
    """ write a string to a text filename """
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
