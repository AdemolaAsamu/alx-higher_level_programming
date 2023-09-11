#!/usr/bin/python3
"""
The module executes a class
That checks if obj is an instance of
A Class
"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of the
    class or inherited by the class
    """

    if isinstance(obj, a_class):
        return True
    return False
