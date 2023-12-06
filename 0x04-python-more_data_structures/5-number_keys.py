#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    k_keys = list(a_dictionary.keys())

    for k in k_keys:
        number += 1

    return (number)
