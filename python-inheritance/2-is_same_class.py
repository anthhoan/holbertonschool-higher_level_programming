#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
        """Returns true if the object is exactly an instance
        the specified class
        """
        return (type(obj) is a_class)
