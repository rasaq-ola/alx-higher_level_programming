#!/usr/bin/python3
"""Defines a simple Rectangle class."""


class Rectangle:
    """Represent a simple rectangle."""

    def __init__(self):
        """Initialize a new rectangle."""
        pass

    @property
    def dict_(self):
        """Return an empty dictionary."""
        return {}


if __name__ == "__main__":
    myrectangle = Rectangle()
    print(type(myrectangle))
    print(myrectangle.dict_)
