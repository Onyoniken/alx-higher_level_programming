#!/usr/bin/python3
"""A class that defining a rectangle"""


class Rectangle:
    """represemting rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes this rectangle class
        Args:
            width: represents the width of a rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: when size is not integer
            ValueError: when size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves a width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets a width attribute"""
        if not isinstance(value, int):
            raise TypeError("width has to be an integer")
        if value < 0:
            raise ValueError("width has to be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves a height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets a height attribute"""
        if not isinstance(value, int):
            raise TypeError("height has to be an integer")
        if value < 0:
            raise ValueError("height has to be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
