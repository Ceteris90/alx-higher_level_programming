#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    len_my_list = len(my_list)

    if idx < 0:
        return None
    if idx => len_my_list:
        return None
    my_list[idx] = element
    return my_list
