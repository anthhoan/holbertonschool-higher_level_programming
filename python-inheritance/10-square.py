#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """initializing a square"""
        self.integer_validator("size", size)
        """integer validator raise typeError or valueError"""
        super().__init__(size, size)
        """super() function that refers to parent class"""
        self.__size = size
