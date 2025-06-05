#!/usr/bin/python3
"""Exploring multiple Inheritance"""

class Fish:
    """class Fish with 2 methods"""
    def swim(self):
        """method swim that prints a string"""
        print("The fish is swimming")

    def habitat(self):
        """method habitat that prints a string"""
        print("The fish lives in water")

class Bird:
    """class Bird with 2 methods"""
    def fly(self):
        """method fly that prints a string"""
        print("The bird is flying")

    def habitat(self):
        """method habitat that prints a string"""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """class FlyingFish that inherits both Fish and Bird"""
    def fly(self):
        """method fly that rewrites the parent class"""
        print("The flying fish is soaring!")

    def swim(self):
        """method swim that rewrites the parent class"""
        print("The flying fish is swimming!")

    def habitat(self):
        """method habitat that rewrites the parent class"""
        print("The flying fish lives both in water and the sky!")

