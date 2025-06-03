#!/usr/bin/python3
"""import ABC and abstractmethod from Abstract Base Classes"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """class Shape that inherits ABC"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """class Circle that inherits Shape"""
    def __init__(self, radius):
        """initializing radius"""
        self.radius = abs(radius)

    def area(self):
        """method toreturn the area of the circle"""
        return ((self.radius ** 2) * math.pi)

    def perimeter(self):
        """method to return the perimeter"""
        return (2 * math.pi * self.radius)

class Rectangle(Shape):
    """"class Rectangle that inherits Shape"""
    def __init__(self, width, height):
        """initializing width and height"""
        self.width = width
        self.height = height

    def area(self):
        """method to return the area"""
        return (self.width * self.height)

    def perimeter(self):
        """method to return the perimeter"""
        return ((self.width * 2) + (self.height * 2))

def shape_info(shape):
    """function that returns area and perimeter through duck typing"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
