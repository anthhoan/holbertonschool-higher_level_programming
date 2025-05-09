#!/usr/bin/python3

if __name__ == "__main__":
    import sys

n = len(sys.argv)
string = sys.argv
i = 0

if n > 2:
    print("{} arguments:".format(n - 1))
else:
    if n > 1:
        print("{} argument:".format(n - 1))
    else:
        if n > 0:
            print("{} arguments.".format(n - 1))

for i in range(1, n):
    print("{}: {}".format(i, string[i]))
