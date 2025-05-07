#!/usr/bin/python3

for tensDigit in range(10):
    for onesDigit in range (tensDigit + 1, 10):
        if tensDigit == 8 and onesDigit == 9:
            print("{}{}".format(tensDigit, onesDigit), end="\n")
        else:
            print("{}{}".format(tensDigit, onesDigit), end=", ")
