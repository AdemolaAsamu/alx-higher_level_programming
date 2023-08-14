#!/usr/bin/python3

def no_c(my_string):
    slit = ""
    x = len(my_string)
    for j in range(x):
        if my_string[j] == 'C' or my_string[j] == 'c':
            continue
        else:
            slit += my_string[j]
    return slit

