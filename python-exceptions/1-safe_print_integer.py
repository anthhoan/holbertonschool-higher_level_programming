#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if type(value) is int:
            print("{}".format(value))
            return (True)
        else:
            if type(value) is str:
                return (False)
    except IndexError:
        pass
