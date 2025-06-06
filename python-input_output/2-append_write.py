#!/usr/bin/python3
"""A function that appends a string at the end of a text file/
returns the number of characters added"""


def append_write(filename="", text=""):
    """append_write function to append a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        """appends to a file a = append"""
        f.write(text)
        number_of_text = len(text)
    return (number_of_text)
