#!/usr/bin/python3
''' Module 9-rectangle.py
Class
Rectangle
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Creates a Rectangle object'''

    # Init private method
    def __init__(self, width, height):
        ''' Creates rectangle object:
            Args:
                width: Private width integer value for Rectangle
                height: Private height integer value for Rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    # Area public method
    def area(self):
        '''Calculate an object's area'''
        return self.__width * self.__height

    # str private method
    def __str__(self):
        '''Return printable representation of a Rectangle object'''
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
