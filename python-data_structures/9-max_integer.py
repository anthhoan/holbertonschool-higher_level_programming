#!/usr/bin/python3

def max_integer(my_list=[]):

    largest = my_list[0]

    for value in my_list:
        if value > largest:
            largest = value
    return (largest)
