#!/usr/bin/python3
"""Module defining a class Student"""

class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dictionary representation of the Student.If list of strings, represents attributes in list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
