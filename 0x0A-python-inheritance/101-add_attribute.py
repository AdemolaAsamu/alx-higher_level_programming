#!/usr/bin/python3
"""
This is a unction for Attribute adding
"""


def add_attribute(obj, attribute, value):
    """
    This either adds or restricts
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
