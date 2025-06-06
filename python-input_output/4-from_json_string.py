#!/usr/bin/python3
"""function that returns a JSON string into a python object"""
import json


def from_json_string(my_str):
    """loads is a function  from pythons built in json module"""
    return json.loads(my_str)
