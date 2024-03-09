#!/usr/bin/python3

"""Define a JSON file/function to string"""

import json

def from_json_string(my_str):
    """Return the string representation of a JSON function"""
    return json.loads(my_str)
