#!/usr/bin/python3
""" Module for creating the Base class """


import json as js
import os
import csv


class Base:
    """ initialize a class with a private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the class and check and raise expection
            Args:
                -id : instance id
        """

        if isinstance(id, (not (None), int)):
            raise TypeError("id must be an integer and Not None")

        if isinstance(id, not (None)):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
