#!/usr/bin/python3
"""
Module for class that inherits from the Int
"""


class MyInt(int):
    """
    Inverts the Int operator == and
    != to perform
    """

    def __eq__(self, value):
        """
        This interchnages the value of operator
        """
        return self.real != value

    def __ne__(self, value):
        """
        this gives the oposite of above
        """
        return self.real == value
