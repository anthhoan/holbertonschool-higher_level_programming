#!/usr/bin/python3
"""Function that writes aa Object to a text file/
using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """w = write/
    dump = used to write a object to text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
