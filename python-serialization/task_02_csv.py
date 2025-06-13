#!/usr/bin/python3
"""Converting CSV Data to JSON format
Reading data from one format (CSV) and converting it into another
format (JSON) using serialization techniques"""
import json
import csv


def convert_csv_to_json(csv_filename):
    """Function that takes the CSV filename as its parameter and
    writes the JSON data to data.json"""
    try:
        """Handling exceptions, such as file not found"""
        with open(csv_filename, "r") as f:
            reader = csv.DictReader(f)
            """DictReader converts each row into a dictionary"""
            data = []
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        return (False)
    
    try:
        with open("data.json", "w", encoding="utf-8") as f:
            """Serialized JSON data to data.json"""
            json.dump(data, f)
    except:
        return (False)
    return (True)
