#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)


"""
    try:
        if type(value) is int:
            print("{:d}".format(value))
            return (True)
        return (False)
    except Exception:
        return (False)

TypeError: Arises when an operation or function is applied/
to an object of an inappropriate type.

ValueError: Raised when a function receives an argument of/
the correct type but an invalid value.
"""
