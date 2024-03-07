#!/bin/python3
"""Defines a function that reads a text file"""

def read_file(filename=""):
    """printing the content of a UTF8 text file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
