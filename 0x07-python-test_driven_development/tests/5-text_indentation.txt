#!/usr/bin/python3
"""
This module executes function to print strings and
put space whenever "?", ".", ":" is encountered
"""


def text_indentation(text):
    """
    Will print and not return error as long
    as it is a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        conditions = ["?", ".", ":"]
        index = 0
        while index < len(text):
            if index == 0:
                print(text[index], end="")
            else:
                true_position = index - 1
                if text[true_position] in conditions and text[index] == " ":
                    index += 1
                    continue
                else:
                    print(text[index], end="")
            for value in conditions:
                if text[index] == value:
                    print()
                    print()
            index += 1
