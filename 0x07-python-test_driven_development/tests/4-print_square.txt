#!/usr/bin/python3
"""
This module runs the function that prints
a rectangle from the #
"""


def print_square(size):
    """
    Simple function that prints the shape
    of a square using # No Gs and Ss
    """

    shape = 0
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    while shape < size:
        print("#" * size)
        shape += 1
