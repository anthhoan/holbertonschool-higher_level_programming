#!/usr/bin/python3
# https://www.geeksforgeeks.org/python-print-common-elements-two-lists/
def common_elements(set_1, set_2):
    common = list(set(set_1) & set(set_2))
    return (common)
