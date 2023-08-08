#!/usr/bin/python3
def uppercase(str):
    output = ""
    for x in str:
        if 'a' <= x <= 'z':
            output += chr(ord(x) - 32)
        else:
            output += x
    print("{}".format(output))
