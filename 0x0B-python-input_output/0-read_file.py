#/usr/bin/python3
""" read text using UTF-8 """


def read_file(filename=""):
    """ read file function """

    with open(filename, encoding='utf-8') as doc:
        read_doc = doc.read()
        print(read_doc, end="")
