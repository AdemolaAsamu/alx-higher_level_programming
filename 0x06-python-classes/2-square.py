#!/usr/bin/python3
"""
lass Square that defines a square by
: (based on 1-square.py)
"""


class Square:
    """
    This is the square class with type error
    and value error handlers
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
