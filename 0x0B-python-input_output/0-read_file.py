#!/usr/bin/python3

def read_file(filename=""):
    """ Reads a txt file and prints to stdout """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
