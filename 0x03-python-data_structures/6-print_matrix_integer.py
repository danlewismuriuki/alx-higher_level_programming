#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for row in matrix:
        for i in range(len(row)):
            num = row[i]
            print("{:d}".format(num), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
