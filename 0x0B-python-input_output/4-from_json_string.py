#!/usr/bin/python3
""" return the object by json string """


import json as jp


def from_json_string(my_str):
    """ return the object by json string """

    return jp.loads(my_str)
