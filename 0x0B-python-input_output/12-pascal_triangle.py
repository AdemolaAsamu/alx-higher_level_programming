#!/usr/bin/python3
"""
This is a Module Housing
A Pascal Triangle Fxn
"""


def pascal_triangle(n):
    """
    Function that prints
    Pascal_Triangle
    """
    if n <= 0:
        return []

    pascal = [[1]]
    size = len(pascal)

    while size < n:
        end = pascal[-1]
        new = [1]
        for i in range(1, len(end)):
            new.append(end[i - 1] + end[i])
        new.append(1)
        pascal.append(new)
    return pascal
