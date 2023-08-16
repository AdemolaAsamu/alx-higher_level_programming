#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = list()
    for row in matrix:
        newMatrix.append(list(map(lambda x: x**2, row)))
    return newMatrix
