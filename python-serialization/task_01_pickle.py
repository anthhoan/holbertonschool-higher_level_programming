#!/usr/bin/python3
"""Pickling Custom Classes
Serialize and Deserialize custom Python objects using the pickle module"""
import pickle


class CustomObject:
    """class CustomObject"""
    def __init__(self, name, age, is_student):
        """initializing name: string, age: string, is_student: bool"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """function that prints Name, Age, and Is_Student"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """serializing a file with pickle
        with try and except errors"""
        try:
            with open(filename, "wb") as f:
                file = pickle.dump(self, f)
        except:
            return (None)

    @classmethod
    def deserialize(cls, filename):
        """deserializing a file with pickle
        with try and except errors"""
        try:    
            with open(filename, "rb") as f:
                file = pickle.load(f)
            return (file)
        except:
            return (None)
