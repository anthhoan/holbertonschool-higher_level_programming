#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    # if len(tuple_a) != len(tuple_b):
    #     return (None)

    return (tuple(x + y for x, y in zip(tuple_a, tuple_b)))
