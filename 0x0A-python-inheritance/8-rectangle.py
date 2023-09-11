#!/usr/bin/python3
"""
This is a module that contains a Class
Rectangle that Builds on Task 7
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a Class Rectangle that inherits from BaseGeometry
    """


    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with a given
        width and height
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
