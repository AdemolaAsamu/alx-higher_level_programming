#!/usr/bin/python3
from sys import argv
if __name__ != "__main__":
    exit()

var = len(argv)

if var == 1:
    var = 0
    print("{} arguments:".format(var - 1) if var > 0
    else "{} arguments.".format(var))
if var > 0:
    for com in range(1, val):
        print("{}: {}".format(com, argv[com]))
