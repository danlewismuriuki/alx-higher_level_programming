#!/usr/bin/python3

def read_file(filename=""):
    """ Reads a txt file and prints to stdout """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
