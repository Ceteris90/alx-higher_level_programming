#/usr/bin/python3
""" write into a file or doc """

def write_file(filename="", text=""):
    """ write into the file """

    with open(filename, 'w+') as doc:
        return doc.write(text)
