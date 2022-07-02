#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return None
    for i, element in enumerate(my_list):
        if i == idx:
            print("Element at index {:d} is {:d}".format(i, element))
