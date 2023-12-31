#!/usr/bin/python3
"""
This module handles the square class
Which is sub to REctangle
"""
from models.rectangle import Rectangle


clase Square(Rectangle):
    """
    This represnts a square by
    referencing points from rect
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This function initilises a new square
        """

        supper().__init__(size, size, x, y, id)

    @property
    def size(Self):
        """
        get the size for the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        property setter
        """
        self.width = value
        self.height = value


    def update(self, *args, **kwargs):
        """
        Update status
        """
        arg = ["id", "size", "x", "y"]
        val = len(args)
        if args and val > 0:
            for num in range(val):
                setattr(self, arg[i], args[i])
        elif kwargs:
            for attr in kwargs:
                setattr(self, attr, kwargs[attr])
        else:
            raise ValueError("update: positional and/or keyword arg required")

    def to_dictionary(self):
        """
        Return the dictnarr
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
    def __str__(self):
        """
        Returns the str and print representation
        of a square
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self,x, self.y, self.width)
