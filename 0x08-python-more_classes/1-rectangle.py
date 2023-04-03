#!/usr/bin/python3
""" Rectangle that defines a rectangle based on 0-rectangle.py """


class Rectangle:
    """
    class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Initialize a class instance
         Args:width (int): the width of the rectangle
        height (int) : the height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be greater 0')
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be greater 0')
        else:
            self.__height = height

    @property
    def width(self):
        """ Return width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if not instance(value, int):
            raise TypeError("Width should be an integer")
        elif value < 0:
            raise ValueError("Width must be greater than 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not instance(value, int):
            raise TypeError("height should be an integer")
        elif value < 0:
            raise ValueError("Height must be greater than 0")
        else:
            self.__height = value
