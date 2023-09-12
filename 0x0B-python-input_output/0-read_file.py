#!/usr/bin/python3
"""
This is a module of function that
reads file and prints to Stdout
"""


def read_file(filename=""):
    """
    This is the function that reads
    a text file
    """

    with open(filename) as content:
        for words in content:
            print(words, end="")
