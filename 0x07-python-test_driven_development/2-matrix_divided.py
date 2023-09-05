#!/usr/bin/python3
"""
Module that handles division of matrix
Returns a new matrix with the answers
"""


def matrix_divided(matrix, div):
    """
    This is a function that handles the
    division of the matrix
    """

    Matlen = []
    buff_list = list()
    index = 0
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    if type(div) != int:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    elif len(matrix) < 1:
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    else:
        for value in matrix:
            Matlen.append(len(value))
        if len(set(Matlen)) != 1:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for array in matrix:
                buff_list.append(list())
                for value in array:
                    if type(value) == int:
                        buff_list[index].append(round(value / div, 2))
                    elif type(value) != int:
                        raise TypeError("matrix must be a matrix (list of lists)\
                                of integers/floats")
                index += 1
        return buff_list
