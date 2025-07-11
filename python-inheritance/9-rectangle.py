#!/usr/bin/python3
"""a class Rectangle the inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """initializing the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        """width being validated by function in parent"""
        self.integer_validator("height", height)
        self.__height = height
        """height being validated by function in parent"""

    def area(self):
        """return the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """return the string of a rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
