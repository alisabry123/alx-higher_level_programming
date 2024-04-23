#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for i in range len(my_list) - 1:
            max_value = my_list[i]
            next_value = my_list[i + 1]
            if max_value < next_value:
                max_value = next_value
            i += 1
            return max_value
