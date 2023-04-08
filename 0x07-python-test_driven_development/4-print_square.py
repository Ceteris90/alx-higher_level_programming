#!/usr/bin/python3
"""
The print_square module for printing a square with the character #.
"""


def print_square(size):
    """Prints a square """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
