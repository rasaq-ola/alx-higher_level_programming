#!/usr/bin/python3
"""
Module 0-add_integer
Defines a function add_integer(a, b) that adds two integers
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers

    Args:
        a: the first number
        b: the second number, defaults to 98 if not provided

    Returns:
        The integer addition of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    return a + b
