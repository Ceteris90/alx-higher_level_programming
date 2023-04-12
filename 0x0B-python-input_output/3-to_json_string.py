#!/usr/bin/python3
""" write and return json file """


import json as js
""" import json module """


def to_json_string(my_obj):
    """ return json represent of my object """

    return js.dumps(my_obj)
