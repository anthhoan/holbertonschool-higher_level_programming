#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """A class representing a Square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of one side of the square (default is 0).
        """
        self.size = size  # This uses the setter for validation

    @property
    def size(self):
        """Getter for the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of square

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of square"""
        return self.__size ** 2
