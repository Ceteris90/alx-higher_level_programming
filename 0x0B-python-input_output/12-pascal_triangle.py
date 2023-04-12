#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Pascal’s triangle of n
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for value_1 in range(1, n):
        row = [1]
        for value_2 in range(1, value_1):
            row.append(triangle[value_1-1][value_2-1] + triangle[value_1-1][value_2])
        row.append(1)
        triangle.append(row)
    return triangle
