#!/usr/bin/python3
"""import abc and abstractmethod from Abstract Base Classes"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """class Animal inherits ABC"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """class Dog that inherits Animal"""
    def sound(self):
        """attribute sound"""
        return ("Bark")

class Cat(Animal):
    """class Cat that inherits Animal"""
    def sound(self):
        """attribute sound"""
        return ("Meow")
