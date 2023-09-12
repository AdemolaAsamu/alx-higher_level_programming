#!/usr/bin/python3
"""
Function that returns the Json
REpresentation of an Obj file
"""
import json


def from_json_string(my_str):
    """
    Produces the json representation
    """
    return json.loads(my_str)
