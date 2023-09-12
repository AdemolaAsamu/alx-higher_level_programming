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

    filetype = 'utf-8'
    with open(filename, "r", encoding=filetype) as file:
        holder = file.read()
        print(holder)
