#!/usr/bin/env python3
def no_c(input_string):
    return ''.join(char for char in input_string if char not in {'c', 'C'})


