#!/usr/bin/python3
''' Access and update private attribute '''


class Square:
    ''' This class defines a square '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''property getter def size(self) to retrieve it'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''property setter def size(self, value) to set size'''
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return(self.__size * self.__size)
