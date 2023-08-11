#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    x = len(argv)
    if x == 1:
    print("{} arguments:".format(x - 1) if x > 0 else "{} arguments.".format(x))
    if x > 0:
        for i in range(1, x):
            print("{}: {}".format(i, argv[i]))
