#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    globsum = 0
    globweight = 0

    for score, weight in my_list:
        globsum += score * weight
        globweight += weight

    if globweight == 0:
        return 0

    return globsum / globweight
