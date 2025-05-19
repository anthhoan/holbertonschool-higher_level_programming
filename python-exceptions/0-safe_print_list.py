#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return (count)

"""
IndexError: Raised when trying to access an index that is out of range in a sequence (e.g., list, tuple).
"""