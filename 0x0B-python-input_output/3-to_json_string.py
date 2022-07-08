#!/usr/bin/python3
"""module converts python object to string"""
import json


def to_json_string(my_obj):
    """converts object to a string"""

    return json.dumps(my_obj)
