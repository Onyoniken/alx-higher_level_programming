#!/usr/bin/python3
for k in range (0, 9):
    for l in range(k + 1, 10):
        if k == 8 and l == 8:
            print("{}{}".format(k, l))
        else:
            print("{}{}".format(k, l), end =", ")
