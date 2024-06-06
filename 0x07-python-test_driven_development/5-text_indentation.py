#!/usr/bin/python3
"""
This module provides a function text_indentation that prints text with 2 new lines after ., ? and :.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters: ., ? and :.
    
    Args:
        text: The text to be processed, must be a string.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = ['.', '?', ':']
    result = ""
    for char in text:
        result += char
        if char in chars:
            result += "\n\n"
    
    lines = result.splitlines()
    for line in lines:
        print(line.strip())
