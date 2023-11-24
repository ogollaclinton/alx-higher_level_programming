#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Reps a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        Args:
            attribs: attributes to represent.
        """
        if (type(attribs) == list and
                all(type(ele) == str for ele in attribs)):
            return {i: getattr(self, i) for i in attribs if hasattr(self, i)}
        return self.__dict__
