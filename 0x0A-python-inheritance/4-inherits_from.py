#!/usr/bin/python3
"""
Module that handles a class
inheritance status
"""


def inherits_from(obj, a_class):
    """
    This checks if it inherited from a subclass
    """

    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False
