#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = list()
    for lists in my_list:
        if (lists % 2) == 0:
            result.append(True)
        else:
            result.append(False)
    return result
