#!/usr/bin/python3
"""
matrix divided my a constant
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    prev_row_len = -1
    new_matrix = []
    for row in matrix:
        if (prev_row_len != len(row) and prev_row_len != -1):
            raise TypeError("Each row of the matrix must have the same size")
            return matrix
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
                return matrix
            else:
                new_matrix.append(round(element / div, 2))
        prev_row_len = len(row)

    return new_matrix
