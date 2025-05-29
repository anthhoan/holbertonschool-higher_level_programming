#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """class MyList with list inheritance"""
    def print_sorted(self):
        """prints a list in ascending order"""
        print(sorted(self))
