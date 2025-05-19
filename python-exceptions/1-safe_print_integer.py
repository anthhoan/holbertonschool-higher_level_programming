#!/usr/bin/python3

def safe_print_integer(value):
    # try:
    #     if type(value) is int:
    #         print("{:d}".format(value))
    #         return (True)
    #     return (False)
    # except Exception:
    #     return (False)
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
