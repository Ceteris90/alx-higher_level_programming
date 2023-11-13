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
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        :param list_dictionaries: List of dictionaries to be converted.
        :return: JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the JSON string representation of list_objs to a file.

        :param list_objs: List of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as my_file:
            if list_objs is None or len(list_objs) == 0:
                my_file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                my_file.write(cls.to_json_string(list_dicts))
    
    @staticmethod
    def from_json_string(json_string):        
        """Returns list from json string"""
        if (json_string is None or len(json_string) == 0):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance from dictionary as an attribute"""
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from file containing json string"""
        my_list = []
        file_name = cls.__name__ + '.json'
        
        if os.path.exists(file_name) is True:
            with open(file_name, 'r') as my_file:
                my_list = cls.from_json_string(my_file.read())
            for i in range(len(my_list)):
                my_list[i] = cls.create(**my_list[i])
        
        return my_list


if __name__ == "__main__":
    pass
