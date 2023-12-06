#!/usr/bin/python3
def uniq_add(my_list=[]):
    q_list = set(my_list)
    number = 0

    for k in q_list:
        number += k

    return (number)
