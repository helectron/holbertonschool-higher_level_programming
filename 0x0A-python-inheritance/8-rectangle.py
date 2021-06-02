#!/usr/bin/python3
'''Module 8-rectangle
Class
    Rectangle
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Creates a Rectangle object
    Methods
        __init__(self, width, height)
    '''

    def __init__(self, width, height):
        '''Creates object
        Arguments
            width: width value integer
            height: height value integer
        '''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
