#!/usr/bin/python3
"""
Appends after a string is found
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Add a string after the line containing the find
    """

    with open(filename) as content:
        para = content.readlines()
    for index, line in enumerate(para):
        if search_string in line:
            para.insert(index + 1, new_string)
    with open(filename, "w") as content:
        content.write("".join(para))
