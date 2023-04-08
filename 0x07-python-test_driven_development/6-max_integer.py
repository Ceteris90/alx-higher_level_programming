#!/usr/bin/env python3
"""
The max_integer module.
"""

def max_integer(lst=[]):
    """Finds and returns, the function returns None.
    """
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")

    if len(lst) == 0:
        return None

    max_val = lst[0]
    for val in lst:
        if val > max_val:
            max_val = val

    return max_val
