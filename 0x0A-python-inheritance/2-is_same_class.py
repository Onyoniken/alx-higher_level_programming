#!/usr/bin/python3
"""Checks an instance of class"""


def is_same_class(obj, a_class):
    """Return true if object is instance
    class, otherwise return false
    """
    return (type(obj) == a_class)
