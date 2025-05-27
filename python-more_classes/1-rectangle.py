#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """a class representing a Rectangle"""
    def __init__(self, width=0, height=0):
        """initializing a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter for the width of square

        Args:
            value (int): The new width to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >=0')
        self.__width = value

    @property
    def height(self):
        """height setter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter for the height of square

        Args:
            value (int): The new height to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >=0')
        self.__height = value
