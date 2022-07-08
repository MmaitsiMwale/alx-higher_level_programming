#!/usr/bin/python3
"""module saves json to file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file"""

    with open(filename, "w") as f:
        return json.dump(my_obj, f)
