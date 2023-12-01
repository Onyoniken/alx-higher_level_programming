#!/usr/bin/python3

def no_c(my_string):
    c_string = ''
    for k in my_string:
        if k != 'c' and k != 'C':
            c_string += k
    return (c_string)
