#!/usr/bin/python3
"""Student to JSON with Filter"""
"""in the json function, if attrs is none it will return itself
else:
it will loop through each dict = object and paste it into a new dictionary
once the loop doesn't find any more objects, it will return the new_dict"""


class Student:
    """class that defines a Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return (self.__dict__)
        else:
            new_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
            return (new_dict)

    def reload_from_json(self, json):
        """reloads values"""
        for attr in json:
            if attr in self.__dict__:
                self.__dict[attr] = json[attr]
