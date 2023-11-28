#!/usr/bin/python3
for k in range(0, 100):
    if k == 99:
        print(f"{k:02d}")
    else:
        print("{:02d}".format(k), end=", ")
