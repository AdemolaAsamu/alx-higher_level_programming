#!/usr/bin/python3
"""
This is a module that executes the class Square
It actually builds off 0-1-2
"""


class Square:
    """
    This is the class Square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Area of the size is calculated
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        This is the getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the setter
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
