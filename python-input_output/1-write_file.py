#!/usr/bin/python3
"""A function that writes to a text file UTF-8 
and returns the number of characters"""


def write_file(filename="", text=""):
    """write_file function"""
    with open(filename, "w", encoding="utf-8") as f:
        """writes to a text file w = write"""
        f.write(text)
        number_of_text = len(text)
    return (number_of_text)
