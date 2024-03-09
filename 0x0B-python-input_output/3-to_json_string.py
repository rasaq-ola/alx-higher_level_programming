#!/usr/bin/python3

"""Coverting a strng to JSON file/function"""

import json

def to_json_string(my_obj):
    """Return the JSON representation of an object(string)"""
    return json.dumps(my_obj)
