#!/usr/bin/python3
"""
Class - Student
"""


class Student:
    """
    This is a student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Initilising the instances
        based on the variables given
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the TOC
        """
        return self.__dict__
