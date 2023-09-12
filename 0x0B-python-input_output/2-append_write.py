#!/usr/bin/python3
"""
This is a module of function that
appends to file and prints len
"""


def append_write(filename="", text=""):
    """
    This is the function that appends to
    a text file if absent create
    """

    with open(filename, 'a', encoding='utf-8') as content:
        content.append(text)
        return len(text)
