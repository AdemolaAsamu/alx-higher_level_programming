#!/usr/bin/python3
"""
This module excites the class MyList
Which inherits from List class
"""


class MyList(list):
    """
    This is the public class which has
    a method def sorted
    """

    def print_sorted(self):
        """
        This function prints a sorted list
        based method for class MyList
        """
        print(sorted(self))
