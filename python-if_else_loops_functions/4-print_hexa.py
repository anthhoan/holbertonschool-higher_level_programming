#!/usr/bin/python3

number = 0

for number in range(99):
    hexadecimal = hex(number)
    print("{} x {}".format(number, hexadecimal))