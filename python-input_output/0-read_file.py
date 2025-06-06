#!/usr/bin/python3
"""A function that reads a text file UTF-8"""


def read_file(filename=""):
    """read_file function"""
    with open(filename, "r", encoding="utf-8") as f:
        """opens the file with r = read"""
        print(f.read(), end="")
    return(f.read())
