#!/usr/bin/python3
"""
Function that returns the Json
REpresentation of an Obj file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Produces the json representation
    """
    with open(filename, 'w') as content:
        json.dump(my_obj, content)
