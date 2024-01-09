#!/usr/bin/python3
"""The module defining class Student"""

class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get representation of Student If list of strings, represents attributes
        included in list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
