#!/usr/bin/python3
'''
This module is a
real definition of a rectangle
'''


class Rectangle:
    '''A class that defines a rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Instantiation
        of an object based on a
        rectangle class
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''retrieves width'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''set the value of width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''set the value of height'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''set the value of height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''rectangle perimeter, addition of all sizes'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''class method for string output'''

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
        for i in range(0, self.__height):
            string += "\n"
            for i in range(0, self.__width):
                string += str(self.print_symbol)
        return string[1:]

    def __repr__(self):
        '''class method for reproducing output'''

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        '''class method to delete instance'''

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
