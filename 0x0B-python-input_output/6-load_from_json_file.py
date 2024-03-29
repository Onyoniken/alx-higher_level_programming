#!/usr/bin/python3
"""This module defining JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates Python object from given JSON file"""
    with open(filename) as f:
        return json.load(f)
