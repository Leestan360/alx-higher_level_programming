#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for a in row:
            print("{:d}".format(a, end=" "))
