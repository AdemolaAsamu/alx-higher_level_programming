#!/usr/bin/python3
"""
This is Module for the First
Rectangle
"""


class Rectangle:
    """
    This is a rectangle class
    """


    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialises a new rectangle
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
