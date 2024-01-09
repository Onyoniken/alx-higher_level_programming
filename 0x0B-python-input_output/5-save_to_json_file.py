#!/usr/bin/python3
"""Module defining JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to txt file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
