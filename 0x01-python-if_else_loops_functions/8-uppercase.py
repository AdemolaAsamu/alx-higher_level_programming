#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        y = ord(str[x])
        upper = chr(y - 32)
        print("{}".format(upper) if y >= 97 and y <= 122
            else "{}".format(str[x]), end="")
    print()
