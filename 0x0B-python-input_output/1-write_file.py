#!/usr/bin/python3
"""module to write to a file"""


def write_file(filename="", text=""):
    """writes to a file"""

    with open(filename, "w") as f:
        return f.write(text)
