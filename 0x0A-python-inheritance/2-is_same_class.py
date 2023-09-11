#!/usr/bin/python3
"""
Module is to excute a Class
That returns a boolean if
the instance is exact
"""


def is_same_class(obj, a_class):
    """"
    Checks if a oarticular object
    is an exact instance of a given class
    """

    if type(obj) != a_class:
        return False
    return True
