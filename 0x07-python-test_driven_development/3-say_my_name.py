#!/usr/bin/python3

"""
Defines a function for printing names.

This function takes a first name and an optional last name

Args:
    first_name (str): The first name to print.
    last_name (str): The last name to print (default is an empty string).

Raises:
    TypeError: If either first_name or last_name are not strings.
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
