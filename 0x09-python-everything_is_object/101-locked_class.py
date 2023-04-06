#!/usr/bin/python3

class LockedClass:
    """Locked class: can't set instance attributes to it
    """
    __slots__ = ('first_name',)

    def __init__(self):
        self.first_name = None
