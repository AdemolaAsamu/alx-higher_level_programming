#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    var = len(argv)
    if var == 1:
        print("{:d} arguments.".format(var - 1))
    elif var > 0:
        for comp in range(1, var):
            print("{:d}: {}".format(comp, argv[comp]))

