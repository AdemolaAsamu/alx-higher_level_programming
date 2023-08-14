#!/usr/bin/python3
def max_integer(my_list=[]):
    x = len(my_list)
    if x == 0:
        return None
    iloc = my_list[0]
    for i in range(x):
        if my_list[i] > iloc:
            iloc = my_list[i]
    return iloc
