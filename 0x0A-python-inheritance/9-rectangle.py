#!/usr/bin/python3
"""
This is a module that contains a Class
Rectangle that Builds on Task 8
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

    def area(self):
        """
        Method returns the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of REctangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
