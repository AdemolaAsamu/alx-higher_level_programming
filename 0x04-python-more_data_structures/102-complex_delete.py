#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    content = list(a_dictionary)
    y = len(content)
    for k in range(y):
        if a_dictionary[content[k]] == value:
            del a_dictionary[content[k]]
    return a_dictionary
