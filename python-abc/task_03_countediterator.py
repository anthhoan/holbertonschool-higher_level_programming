#!/usr/bin/python3
"""class CountedIterator that extends the built in iterator obtained/
from the iter function."""


class CountedIterator:
    """class CountedIterator"""
    def __init__(self, some_iterable):
        """two attributes, the iterator object, and a counter"""
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """return the current value of the counter"""
        return (self.count)

    def __next__(self):
        """next method raises a StopIteration exception when there are no/
        more items to iterate"""
        try:
            item = next(self.iterator)
            self.count += 1
            return (item)
        except StopIteration:
            raise StopIteration("No more items to iterate")
