#!/usr/bin/python3
def uppercase(str):
    output = ""
    for x in str:
        if x >= 97 or x <= 122:
            output += chr(ord(x) - 32)
        else:
            output += x
    print("{}".format(output), end="")
