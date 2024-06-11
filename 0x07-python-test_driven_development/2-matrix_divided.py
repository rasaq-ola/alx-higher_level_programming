#!/usr/bin/python3
"""
This module provides a function matrix_divided that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns the new matrix.
    
    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide the matrix elements by.
    
    Raises:
        TypeError: If matrix elements are not integers/floats or rows are not of the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    
    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(x / div, 2) for x in row] for row in matrix]
