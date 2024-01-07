#!/usr/bin/python3
""""

The module contains function which prints a name

"""


def say_my_name(first_name, last_name=""):
    '''The function prints name (<first name> <last name>)

    Args:
        first_name (str):fisrt name to be printed
        last_name (str):last name to be printed

    Raises:
        TypeError: If either the first_name and last_name are not strings

    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name to be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name to be a string")
    print(f"My name is {first_name} {last_name}")
