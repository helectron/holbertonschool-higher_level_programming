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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
