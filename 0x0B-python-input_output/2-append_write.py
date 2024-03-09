#!/usr/bin/python3
"""A ile appending function"""

def append_write(filename="", text=""):
    """Appends a string at the end of a text file.

    Args:
    filename (str): The name of the file to append to
    tet (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return f.write(text)
