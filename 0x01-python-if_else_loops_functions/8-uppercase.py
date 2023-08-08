#!/usr/bin/python3
def uppercase(str):
    output = ""
    for x in str:
        if 97 <= x <= 122:
            output += chr(ord(x) - 32)
        else:
            output += x
    print("{}".format(output), end="")
