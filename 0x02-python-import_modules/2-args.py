#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    col = len(argv)
    if col == 1:
        col = 0
    print("{} arguments:".format(col - 1) if col > 0
            else "{} arguments.".format(col))
    if col > 0:
        for i in range(1, col):
            print("{}: {}".format(i, argv[i]))
