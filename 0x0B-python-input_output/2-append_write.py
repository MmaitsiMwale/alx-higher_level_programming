#!/usr/bin/python3
"""module appends to a file"""


def append_write(filename="", text=""):
    """appends to a file"""

    with open(filename, "a") as f:
        return f.write(text)
