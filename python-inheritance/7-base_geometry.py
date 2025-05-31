#!/usr/bin/python3
"""Improve Geometry"""


class BaseGeometry:
    """class BaseGeometry"""

    """Public instance method"""
    def area(self):
        """raise an Exception with a message"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if not isinstance(value, int):
            """raise TypeError with message"""
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            """raise ValueError with message"""
            raise ValueError("{} must be greater than 0".format(name))
