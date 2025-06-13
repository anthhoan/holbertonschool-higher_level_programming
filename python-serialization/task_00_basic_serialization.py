#!/usr/bin/python3
"""Basic serialization
Creating a basic serialization module that adds the functionality to serialize a
Python dictionary to a JSON file and deserialize te JSON file to recreate
the Python Dictionary"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to a specified file"""
    with open(filename, "w", encoding="utf-8") as f:
        file = json.dumps(f)
        return (file)

def load_and_deserialize(filename):
    """Load and deserialize data from the specified file"""
    with open (filename, "r", encoding="utf-8") as f:
        file = json.loads(f)
        return (file)
