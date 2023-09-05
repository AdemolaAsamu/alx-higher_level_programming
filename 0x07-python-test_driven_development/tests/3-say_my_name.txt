#!/usr/bin/python3
"""
This is a module that executes the
function that prints out name
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints first and last name
    It also raises value Errore if not string
    """

    if first_name is None:
        raise TypeError("first_name must be a string")
    elif last_name is None:
        raise TypeError("last_name must be a string")
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
