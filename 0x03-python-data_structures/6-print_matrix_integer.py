#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if (column < len(matrix[row]) - 1):
                print("{}".format(matrix[row][column]), end=" ")
            else:
                print("{}".format(matrix[row][column]))
