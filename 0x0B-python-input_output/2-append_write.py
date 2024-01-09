#!/usr/bin/python3
"""This a module defining file-appending function."""


def append_write(filename="", text=""):
    """Appends string to end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
