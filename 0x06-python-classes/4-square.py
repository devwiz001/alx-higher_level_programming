#!/usr/bin/python3

"""this define a class Square."""


class Square:
    """this represent a square."""

    def __init__(self, size=0):
        """this initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """this Get or set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """simply return the current area of the square."""
        return (self.__size * self.__size)
