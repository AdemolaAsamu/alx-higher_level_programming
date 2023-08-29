#!/usr/bin/python3
"""
This is a module that executes the class Square
It actually builds off 0-1-2
"""


class Square:
    """
    This is the class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Gets the attribute of the positions"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets attributes
        """
        if type(value) != tuple or len(value) != 2 \
                or type(value[0]) != int or type(value[1]) != int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tupple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        This is a printer
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
