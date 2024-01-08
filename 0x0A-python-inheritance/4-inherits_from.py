#!/usr/bin/python3
"""checks whether  object is an instance of a class that's inherited
"""


def inherits_from(obj, a_class):
    """Returns true if object is inherited class otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
