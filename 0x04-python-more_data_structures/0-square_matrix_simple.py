#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    other_matrix = []
    for i in matrix:
        other_matrix.append(list(map(lambda x: x ** 2, i)))
    return other_matrix
