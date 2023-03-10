#!/usr/bin/python3

def remove_char_at(str, n):
    for i in range(0, len(str)):
        if i != n:
            print(str[i], end = '')

remove_char_at("Jonas is Good",2)
