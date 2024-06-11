#!/usr/bin/python3
"""
This module defines a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers.

    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
        ValueError: If either `a` or `b` is NaN or infinite.

    Returns:
        int: The sum of `a` and `b`, casted to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (a != a or a in (float('inf'), -float('inf'))):
        raise ValueError("cannot convert float NaN or infinite to integer")
    if isinstance(b, float) and (b != b or b in (float('inf'), -float('inf'))):
        raise ValueError("cannot convert float NaN or infinite to integer")

    return int(a) + int(b)
