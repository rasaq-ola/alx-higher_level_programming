#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square.

    Private instance attribute:
        __size: size of the square.
    """
    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
