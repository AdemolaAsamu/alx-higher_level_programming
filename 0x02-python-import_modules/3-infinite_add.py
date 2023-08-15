#!/usr/bin/python3
from sys import argv


def retro(*args):
    sum = 0
    size = len(args)
    if size == 0:
        print("{}".format(sum))
    else:
        for i in range(0, size):
            sum += int(args[i])
        print("{}".format(sum))


if __name__ == '__main__':
    retro(*argv[1:])
