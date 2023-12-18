#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as k:
        print("Exception: {}".format(k), file=sys.stderr)
        return None
