#!/usr/bin/python3
"""Extending the Python List with Notifications"""


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
        """pop a index from a list"""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
