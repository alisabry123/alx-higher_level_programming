#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    new_list[:] = my_list[:]
    if idx >= 0 and idx <= len(my_list) - 1:
        new_list[idx] = element
        return new_list
    else:
        return my_list
