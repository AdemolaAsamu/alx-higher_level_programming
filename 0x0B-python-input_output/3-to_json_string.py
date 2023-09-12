#!/usr/bin/python3
"""
Function that returns the Json
REpresentation of an Obj file
"""
import json


def to_json_string(my_obj):
    """
    Produces the json representation
    """
    
    return json.dumps(my_obj)
