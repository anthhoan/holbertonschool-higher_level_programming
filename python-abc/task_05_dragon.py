#!/usr/bin/python3
"""Mastering MixIns"""

class SwimMixin:
    """class SwimMixin"""
    def swim(self):
        """method Swim that prints a string"""
        print("The creature swims!")

class FlyMixin:
    """class FlyMixin"""
    def fly(self):
        """method fly that prints a string"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """class Dragon that inherits SwimMixin and FlyMixin"""
    def roar(self):
        """method roar that prints a string"""
        print("The dragon roars!")
