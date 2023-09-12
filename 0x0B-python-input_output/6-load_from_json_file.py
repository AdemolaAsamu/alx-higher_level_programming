#!/usr/bin/python3
"""
Function that returns the Json
REpresentation of an Obj file
"""
import json


def load_from_json_file(filename):
    """
    Loads from a Json file presentation
    """
    with open(filename, 'r') as content:
        return json.load(content)
