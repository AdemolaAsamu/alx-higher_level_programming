#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    var = len(argv)
    if var == 1:
        print("{:d} arguments.".format(var - 1))
    elif var == 2:
        print("{:d} arguments:".format(var - 1))
        print("{:d}: {}".format(var - 1, argv[1]))
    else:
        print("{:d} arguments:".format(var - 1))
        for x in range(1, var):
            print("{:d}: {}".format(var, argv[var]))

