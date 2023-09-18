#!/usr/bin/python3
"""
This is Module for the First
Rectangle
"""
from models.base import Base


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

    def __str__(self):
        """
        string representation of instances
        """
        return (f"[{self.__class__.__name__}] ({self.id})"
                f"{self.__x}/{self.__y} - self.__width}/{self.__height}")

    @property
    def width(self):
        """
        property getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        property setter for width
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        property getter for height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        property setter for height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            rasie ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Property getter for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        property setter for x
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x  = x

    @property
    def y(self):
        """
        property getter for y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter for y variable
        """
        if type(y) != int:
            rasie TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        function that calculates area or rectablge
        """
        return self.__width * self.__height

    def display(self)
    """
    printing the rectangle in form of a string
    """
    for num in range(self.__y):
        print("")
    x = " " * self.__x
    p = x + "#" * self.__width
    for num in range(self.__height):
        print(p)

    def update(self, *args, **kwargs):
        """
        update to Rectangle Attributes
        """

        args = ["id", "width", "height", "x", "y"]
        val = len(args)
        if args and val > 0:
            for i in range(val):
                setattr(self, arg[i], args[i])
        elif kwargs:
            for attr in kwargs:
                setattr(self, attr, kwards[attr])
        else:
            raise ValueError("update: positional and/or keyword arg required")

    def to_dictionary(self):
        """
        This gets the dict representation for a rectangle
        """

        return {
                "id": self.id, "width": self.width,
                "height": self.height, "x": self.x,
                "y": self.y
        }
