#!/usr/bin/python3
"""
copy a list
"""


def copy_list(l):
    """generates a copy of a list
    """
    if not isinstance(l, list):
        return None
    return l[:]
