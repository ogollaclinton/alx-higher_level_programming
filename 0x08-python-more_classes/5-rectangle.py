#!/usr/bin/python3
'''class rectangle'''


class Rectangle:
    '''str rep'''
    def __init__(self, width=0, height=0):
        '''
        Args:
        width: width of rectangle.
        height: height of rectangle.

        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        if not self.width or not self.height:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
