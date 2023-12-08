#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None

    large = matrix[0][0]
    for row in matrix:
        for element in row:
            if large < element:
                large = element

    return large
