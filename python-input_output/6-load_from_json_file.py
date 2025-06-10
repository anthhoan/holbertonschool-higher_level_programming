#!/usr/bin/python3
"""Create object from JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        """open filename with r = read only"""
        return json.load(f)
        """json.load() takes a file object and returns the json object"""
