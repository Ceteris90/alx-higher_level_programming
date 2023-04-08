#!/usr/bin/python3
"""
The text_indentation module.
"""


def text_indentation(text):
    """ Adds two newlines """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
