#!/usr/bin/python3
""" returns the dictionary description with simple data structure """


def class_to_json(obj):
    """ create a function class from a json """

    return obj.__dict__
