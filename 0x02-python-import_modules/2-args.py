#!/usr/bin/python3
if __name__ != '__main__':
    exit()
if __name__ == '__main__':
    from sys import argv
    x = len(argv)
    y = x - 1
    if x == 1:
        x = x - 1
    print("{} arguments:".format(y) if x > 0 else "{} arguments.".format(x))
    if x > 0:
        for i in range(1, x):
            print("{}: {}".format(i, argv[i]))
