#!/usr/bin/python3
"""
add two integers
"""


def add_integer(a, b=98):
    """ Check that both arguments are either integers or floats """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    """ Convert the arguments to integers and add them """
    result = int(a) + int(b)
    return result
