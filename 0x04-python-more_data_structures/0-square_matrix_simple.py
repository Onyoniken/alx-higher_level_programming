#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    k_matrix = matrix.copy()

    for k in range(len(matrix)):
        k_matrix[k] = list(map(lambda x: x**2, matrix[k]))

    return (k_matrix)
