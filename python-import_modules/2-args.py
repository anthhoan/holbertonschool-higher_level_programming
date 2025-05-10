#!/usr/bin/python3

if __name__ == "__main__":
    import sys

n = len(sys.argv) - 1
string = sys.argv
i = 0

if n >= 2:
    print("{} arguments:".format(n))
else:
    if n == 1:
        print("{} argument:".format(n))
    else:
        if n == 0:
            print("{} arguments.".format(n))

for i in range (1, n + 1):
    print("{}: {}".format(i, string[i]))
