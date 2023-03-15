#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest = []
    for index in my_list:
        biggest.append(index)

    return max(biggest)
