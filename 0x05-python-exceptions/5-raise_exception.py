#!/usr/bin/python3

def raise_exception():
    sum = 0
    try:
        sum ** 'cat'
    except TypeError:
        raise
