#!/usr/bin/python3
"""
Creates an Object from a “JSON file”.
"""


import json as jp


def load_from_json_file(filename):
    """
    Creates an object from filename.
    """

    with open(filename, 'r') as doc:
        return jp.load(doc)
