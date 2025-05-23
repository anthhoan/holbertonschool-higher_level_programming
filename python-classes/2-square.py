#!/usr/bin/python3
"""class Square with TypeError and ValueError(s)"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """__init__ initializes the square

        Attributes:
            size: The private size of a square

        Errors:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >=0')
        self.size = size
