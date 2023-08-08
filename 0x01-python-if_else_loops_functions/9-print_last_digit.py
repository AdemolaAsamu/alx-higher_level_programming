#!/usr/bin/python3
def print_last_digit(number):
    x = number
    if x >= 0:
        x = x % 10
        return x
    else:
        x = (-1 * x) % 10
    return x
