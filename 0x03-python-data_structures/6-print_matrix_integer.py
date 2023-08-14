#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for row in matrix:
            i = len(row) - 1
            k = len(row)
            for j in range(k):
                if j < i:
                    print("{:d}".format(row[j]), end=" ")
                else:
                    print("{:d}".format(row[j]))
