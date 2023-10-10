#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxm_int = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxm_int:
            maxm_int = my_list[i]
            return maxm_int
