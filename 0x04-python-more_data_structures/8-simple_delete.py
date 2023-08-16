#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for items in list(a_dictionary):
        if key == items:
           del a_dictionary[key]
    return a_dictionary
