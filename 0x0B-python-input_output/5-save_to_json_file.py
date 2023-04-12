#!/usr/bin/python3
""" write an object to a text file using JSON """


import json as jp


def save_to_json_file(my_obj, filename):
    """ save text to a file json file """

    with open(filename, 'w+') as doc:
        jp.dump(my_obj, doc)
