#!/usr/bin/python3
def uppercase(str):
    for k in str:
        if ord("a") <= ord(k) <= ord("z"):
            k = chr(ord(k) - 32)
        print("{:s}".format(k), end="")
    print()
