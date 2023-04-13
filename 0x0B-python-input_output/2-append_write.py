#!/usr/bin/python3
""" append a string at the end of text file """


def append_write(filename="", text=""):
    """ append a string text file """

    with open(filename, "a+", encoding="UTF-8") as doc:
        return doc.write(text)
