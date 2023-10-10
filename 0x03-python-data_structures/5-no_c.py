#!/usr/bin/env python3
def no_c(my_string):
    str2 = my_string.translate({ord(i): None for i in 'cC'})
    return str2
