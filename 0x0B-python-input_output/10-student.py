#!/usr/bin/python3
"""
Creates a Student class.
"""


class Student:
    """Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        """

        my_dictionary = dict()
        if type(attrs) is list and all(type(value) is str for value in attrs):
            for value in attrs:
                if value in self.__dict__:
                    my_dictionary.update({value: self.__dict__[value]})
            return my_dictionary
        return self.__dict__.copy()
