#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
This module contains a function to rotate
a given 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise.
    Args:
        matrix (list[list]): The input matrix.
    Returns:
        None. The matrix is rotated in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
