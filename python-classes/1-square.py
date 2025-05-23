#!/usr/bin/python3
"""class Square with private instance attribute size"""


class Square:
    """class Square"""
    def __init__(self, size):
        """__init__ initializes the square

        Attributes:
            size: The private size of the square
        """
        self.__size = size
