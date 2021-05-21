#!/usr/bin/python3
'''
This module creates an
empty class Rectangle
'''


class Rectangle:
    '''A class that defines a rectangle'''
    def __init__(self, width=0, height=0):
        '''Instantiation
        of an object based on a
        rectangle class
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''gets, retrieves width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the value of width'''
        self.__width = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''set the value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the value of height'''
        self.__height = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
