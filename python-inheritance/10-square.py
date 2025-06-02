#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """initializing a square"""
        super().__init__(size, size)
        """super() function that refers to parent class"""