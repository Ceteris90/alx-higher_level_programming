#!/usr/bin/python3
def element_at(my_list, idx):
    len_my_list = len(my_list)
    for index in my_list:
        if idx < 0:
            return None
        elif idx > len_my_list:
            return None
        else:
            return my_list[idx]
