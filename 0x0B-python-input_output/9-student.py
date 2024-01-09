#!/usr/bin/python3
"""Module defining class Student"""


class Student:
    """Representing student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets dictionary representation of the Student"""
        return self.__dict__
