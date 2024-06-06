#!/usr/bin/python3
"""
This module provides a function add_integer that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    
    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float, defaults to 98.
    
    Raises:
        TypeError: If a or b are not integers or floats.
    
    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
