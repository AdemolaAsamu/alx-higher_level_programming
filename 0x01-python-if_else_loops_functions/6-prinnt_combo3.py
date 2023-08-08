#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if y > x:
            if y == 9 and x == 8:
                print("{}{}".format(x, y))
            else:
                print("{}{}, ".format(x, y), end="")
