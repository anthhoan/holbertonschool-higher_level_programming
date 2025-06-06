#!/usr/bin/python3
"""A function that writes to a text file UTF-8"""

def write_file(filename="", text=""):
    """write_file function"""
    with open(filename, "w", encoding="utf-8") as f:
        """writes to a text file w = write"""
        f.write(text)
    return (f.write(text))
