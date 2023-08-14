#!/usr/bin/python3
def multiple_returns(sentence):
    y = len(sentence)
    if y == 0:
        return (y, None)
    else:
        return (y, sentence[0])
