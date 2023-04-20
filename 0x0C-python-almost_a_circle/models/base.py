#!/usr/bin/python3
""" Module for creating the Base class """


import json
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

        if not isinstance(id, (int, None)):
            raise TypeError("id must be an integer and Not None")

        if not isinstance(id, None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
