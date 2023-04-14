#!/usr/bin/python3
"""object is an instance of a class that inherited
(directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """obj is an instance of a class that
    inherited from a_class.
    """

    return isinstance(obj, a_class) and type(obj) != a_class
