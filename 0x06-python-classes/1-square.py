#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square.

    Private instance attribute:
        __size: size of the square.
    """
    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
