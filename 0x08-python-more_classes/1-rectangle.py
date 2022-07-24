#!/usr/bin/python3
"""defines a rectangle of width=width and height=height"""


class Rectangle:
    """defines a rectangle of width=width and height=height"""

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
