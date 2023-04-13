#!/usr/bin/python3
"""
Finds object exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """Function to determine if obj is an instance
    """
    if isinstance(type(obj), a_class):
        return (True)
    else:
        return (False)
