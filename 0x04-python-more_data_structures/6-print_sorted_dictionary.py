#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_k = list(a_dictionary.keys())
    list_k.sort()
    for k in list_k:
        print("{}: {}".format(k, a_dictionary.get(k)))
