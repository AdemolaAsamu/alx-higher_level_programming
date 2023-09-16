#!/usr/bin/python3
"""
This is the base case that
is called by the modules
"""


class Base:
    """
    This is a base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        this is the function check
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
