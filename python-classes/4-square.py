#!/usr/bin/python3
"""Defines a class square"""

class Square:
    """Represents a square with a size.
    Provides methods to get/set the size and calculate the area.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of one side of the square (default is 0).
        """
        self.size = size  # This uses the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

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
        """Calculate and return the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2
