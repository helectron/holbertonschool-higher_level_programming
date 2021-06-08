#!/usr/bin/python3
'''
Subclass rectangle inherits
from Base class
'''

from models.base import Base


class Rectangle(Base):
    ''' constructor '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Retrieve the with of Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        '''Retrieve the with of Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        '''Retrieve the with of Rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        '''Retrieve the with of Rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        '''returns the area of a rectangle'''
        return self.height * self.width