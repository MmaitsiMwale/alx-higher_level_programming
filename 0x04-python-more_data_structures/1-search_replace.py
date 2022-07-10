#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = my_list[:]
    for idx, el in enumerate(new):
        if el == search:
            my_list[idx] = replace
