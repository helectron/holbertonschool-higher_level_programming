#!/usr/bin/python3
'''Module 10-square
Classes
    Square
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Creates a Rectangle object
    inherits from Rectangle
    '''

    def __init__(self, size):
        ''' Creates square object :
            Args:
                size (int): Value for the Square object
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Calculate rectangule´s area'''
        return super().area()
