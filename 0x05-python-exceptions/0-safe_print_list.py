#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # This func writes a function that prints x elements of a list.
    try:
        count_num = 0
        for i in range(x):
            print(my_list[i], end="")
            count_num = count_num + 1
        print()
        return count_num
    except IndexError:
        print()
        return count_num
