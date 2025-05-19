#!/usr/bin/python3

def safe_print_integer(value):
    try:
        val = int(value)
        print("{:d}".format(val))
        return (True)
    except (ValueError, TypeError):
        return (False)

    # try:
    #     if type(value) is int:
    #         print("{:d}".format(value))
    #         return (True)
    #     return (False)
    # except Exception:
    #     return (False)
