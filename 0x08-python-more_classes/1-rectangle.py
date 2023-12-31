#!/usr/bin/python3
"""A class that defining a rectangle"""


class Rectangle:
    """this represents rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes this rectangle class
        Args:
            width: representing rectangle width
            height: represents rectangle height
        Raises:
            TypeError: if size not an integer
            ValueError: if size less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width has to be an integer")
        if value < 0:
            raise ValueError("width has to be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height has to be an integer")
        if value < 0:
            raise ValueError("height has to be be >= 0")
        self.__height = value
