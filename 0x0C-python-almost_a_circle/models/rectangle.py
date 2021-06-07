#!/usr/bin/python3
'''
Subclass rectangle inherits
from Base class
'''

from models.base import Base


class Rectangle(Base):
    ''' constructor '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Retrieve the with of Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        self.size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def height(self):
        '''Retrieve the with of Rectangle'''
        return self.__height

    @width.setter
    def height(self, value):
        self.size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def x(self):
        '''Retrieve the with of Rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        self.size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def y(self):
        '''Retrieve the with of Rectangle'''
        return self.__height

    @y.setter
    def height(self, value):
        self.size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
