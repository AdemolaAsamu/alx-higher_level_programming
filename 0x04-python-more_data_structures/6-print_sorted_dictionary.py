#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys, items in sorted(a_dictionary.items()):
        print("{}: {}".format(keys, items))
