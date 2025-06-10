#!/usr/bin/python3
"""function that creates an Object from JSON file"""
import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        """open filename with r = read only"""
        json.load(filename)
        """json.loaf() takes a file object and returns the json object"""
