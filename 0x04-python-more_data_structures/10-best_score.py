#!/usr/bin/python3
def best_score(a_dictionary):
    highest = 0
    best_student = ""
    if a_dictionary is not None:
        for keys, values in a_dictionary.items():
            if values > highest:
                best_student = keys
                highest = values
    else:
        return None
    return best_student
