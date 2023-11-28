#!/usr/bin/python3
for k in range (9):
    for l in range(k + 1, 10):
        if k * 10 + l < 89:
            print("{:d}{:d}".format(k, l), end=",")
        print("{:d}".format(89))
