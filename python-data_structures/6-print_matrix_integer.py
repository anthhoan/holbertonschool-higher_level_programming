#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if len(matrix) == 0:
        return (None)

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            # if i'm not the last one in the array, print a space after the digit 
            if column != (len(matrix[column]) - 1):
                print("{:d}".format(matrix[row][column]), end=" ")
            # else, print
            else:
                print("{:d}".format(matrix[row][column]), end="")
        print()
