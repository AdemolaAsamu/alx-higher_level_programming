#!/usr/bin/python3
"""
This is the module executing the Rectangle
Class with getters and setters
"""


class Rectangle:
    """
    This states the getters and setters to be created
    Also an area function does the area and perimeter
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int or type(value) is None:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int or type(value) is None:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        if self.__width == 0 and self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + 
                ("\n" + str(self.print_symbol) * self.__width) * (self.__height - 1))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter
