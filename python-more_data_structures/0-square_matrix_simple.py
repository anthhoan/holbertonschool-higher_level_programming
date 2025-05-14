#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = []

    if len(matrix) > 0:
        # matrix[:] is a common way to create a copy of an entire matrix
        for number in matrix[:]:
            new_matrix.append(list(map(lambda x: x ** 2, number)))
        return new_matrix
