#!/usr/bin/python3
"""The module define Python class-to-JSON function"""


def class_to_json(obj):
    """Return the dictionary representation of simple data structure"""
    return obj.__dict__
