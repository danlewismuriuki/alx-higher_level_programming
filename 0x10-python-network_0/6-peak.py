#!/bin/bash

def find_peak(list_of_integers):
    # Check for empty array
    if list_of_integers == []:
        return None

    #get length of the array
    size = len(list_of_integers)

    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    # Divide the list length
    mid_size = int(size/2)

    #Assume the midsize is the peak
    peak_array = list_of_integers[mid_size]

    # check right and left adjacents to the mid value
    if peak_array > list_of_integers[mid_size - 1] and peak_array > list_of_integers[mid_size + 1]:
        return peak_array

    # if peak is less than right value recurse and check
    # values from mid to start else
    elif peak_array < list_of_integers[mid_size - 1]:
        return find_peak(list_of_integers[:mid_size])
    else:
        return find_peak(list_of_integers[mid_size + 1:])
