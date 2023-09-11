#!/usr/bin/python3
"""
Module executes Class Square which inherits
from Task 9 Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initialises with size
        """

        super().__init__(size, size)

        self.__size = size
