#!/usr/bin/python3

def add_integer(a, b=98):

    a = int(a)
    b = int(b)

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be integer')
    
    return (a + b)
