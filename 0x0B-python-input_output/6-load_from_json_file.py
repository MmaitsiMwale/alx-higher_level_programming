#!/usr/bin/python3
"""module loads file from json"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, "r") as f:
        return json.load(f)
