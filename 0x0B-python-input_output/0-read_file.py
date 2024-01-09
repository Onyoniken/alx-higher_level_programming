#!/usr/bin/python3
"""The module defining text file-reading function"""


def read_file(filename=""):
    """Prints UTF8 text file content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
