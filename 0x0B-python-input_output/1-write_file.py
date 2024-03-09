#!/usr/binipython3
"""A file writting  function."""
def write_fle(filename="", text=""):
    """write a string to a UTF8 text file.

    Args:
    filename (str): The name of the file to write.
    text (str): The text to write to the file.
    Returns:
    The numberof characters written.
    """
    with open(filename, encoding="utf-8") as f:
        return f.write(text)
