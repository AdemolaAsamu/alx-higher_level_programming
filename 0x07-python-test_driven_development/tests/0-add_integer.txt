#!/usr/bin/python3
"""
This Module Executes Task 0 in the ALx Task 
Test Driven DEvelopment. This add 2 numbers floats
and Integers and raises typeerror in case
"""


def add_integer(a, b=98):
    """
    This is the function that accepts the two
    variables a and b initialised If float rounds
    off to int and if not raises TypeError or Value
    Error Accordingly
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
