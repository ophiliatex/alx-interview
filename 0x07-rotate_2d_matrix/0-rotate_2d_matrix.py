#!/usr/bin/python3
"""
The module contain the functions for rotating the 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the 2D matrix by 90 degrees.
    :param matrix:
    :return:
    """
    N = int(len(matrix))

    for i in range(N):
        for j in range(i + 1, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(N):
        matrix[i].reverse()
