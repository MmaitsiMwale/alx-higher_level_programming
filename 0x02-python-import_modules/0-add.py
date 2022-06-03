#!/usr/bin/python3

if _name__ == "__main__":
    """prints the sum of two numbers"""
    from add_0 import add

    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
