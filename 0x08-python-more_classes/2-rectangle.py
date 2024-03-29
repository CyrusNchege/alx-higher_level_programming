#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
        args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

        @property
        def width(self):
            """Get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """Set the width of the rectangle"""
            if not isinstance(value, int):
                 raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """Get the height of the rectangle"""
            return self.__height
        
        @height.setter
        def height(self, value):
            """Set the height of the rectangle"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

        def area(self):
            """Return the area of the rectangle"""
            return self.__width * self.__height

        def perimeter(self):
            """Return the perimeter of the rectangle"""
            if self.__width == 0 or self.__height == 0:
                return 0
            else:
                 return 2 * (self.__width + self.__height)
