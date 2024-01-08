#!/usr/bin/python3
"""Defines a base geometry"""


class BaseGeometry:
    """the class represents a base geometry"""

    def area(self):
        """method hasn't been implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
