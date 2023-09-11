#!/usr/bin/python3
"""
This is a module that contains
a class base grometry
Builds on Task 6
"""


class BaseGeometry:
    """
    This is a Class BaseGgeometry
    """

    def area(self):
        """
        Public instance method area(self)
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance that confirms the
        Type of value inputed
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
