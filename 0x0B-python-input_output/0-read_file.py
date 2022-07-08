#!/usr/bin/python3
"""module to read a file"""


def read_file(filename=""):
    """reads a file"""

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
