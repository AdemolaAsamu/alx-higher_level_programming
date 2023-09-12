#!/usr/bin/python3
"""
This is a module of function that
writes to file and prints len
"""


def write_file(filename="", text=""):
    """
    This is the function that writes
    a text file if absent create
    """

    with open(filename, 'w', encoding='utf-8') as content:
        content.write(text)
        return len(text)
