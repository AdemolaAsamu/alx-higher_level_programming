#!/usr/bin/python3

def roman_to_int(roman_string):
    intval = 0
    vault = {"M": 1000, "D": 500, "C": 100,
            "L": 50, "X": 10, "V": 5, "I": 1}
    test = isinstance(roman_string, str)
    if roman_string is None or test != True:
        return intval
    x = len(roman_string) - 1
    for y in range(x):
        if vault.get(roman_string[y]) < vault.get(roman_string[y + 1]):
            intval -= vault.get(roman_string[y])
        else:
            intval += vault.get(roman_string[y])
    intval += vault.get(roman_string[x]) 
    return intval
