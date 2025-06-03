#!/usr/bin/python3
"""Extending the Python List with Notifications
the built in list class has multiple methods such as
append, extend, insert, remove, pop, clear, sort, reverse.
We use super() because it calls on the original method() from the parent class List"""


class VerboseList(list):
    """class Verbose that inherits built in list class"""
    def append(self, item):
        """appending to a list"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """extend the list with number of items"""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """remove item from list"""
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """pop a index from a list
        index=-1 is a default that aligns with pythons built in behavior
        the original pop() method removes and returns"""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return (item)
