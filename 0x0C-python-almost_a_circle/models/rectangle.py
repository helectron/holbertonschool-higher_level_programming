#!/usr/bin/python3
'''
module rectangle
Class
    Rectangle
'''

from models.base import Base


class Rectangle(Base):
    '''
    Creates a Rectangle object
    ...
    Properties
    ----------
        width (int): width of the instance
        height (int): height of the instance
        x (int): x coordenate
        y (int): y coordenate
        id (int): object identificator
    Methods
    -------
        __init__(self, width, height, x=0, y=0, id=None)
        def area(self)
        display(self)
    Magic Methods
    -------------
        __str__(self)
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor
        Id parameter is set by the superclass `Base`
        Arguments:
            width (int): width of the instance
            height (int): height of the instance
            x (int): x coordenate
            y (int): y coordenate
            id (int): object identificator
        '''
        super().__init__(id)
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
        '''sets width'''
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        '''Retrieve the height of Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Retrieve the height of Rectangle'''
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        '''Return x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Sets x'''
        self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        '''Return y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets y'''
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    # Methods
    def area(self):
        '''returns the area of a rectangle'''
        return self.height * self.width

    def display(self):
        '''
        print to stdout the graphic representation
        of the object taking x and y as reference
        to the position of the object in the screen
        '''
        print("\n" * self.__y, end='')
        for iterator in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    # Magic method
    def __str__(self):
        '''
        overriding the __str__ method so that it returns
        `[Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''
        return ("[{}] ({}) {}/{} - {}/{}".format
                (__class__.__name__, self.id, self.x,
                    self.y, self.width, self.height))

    def update(self, *args):
        '''
        Update the object's attributes
        Arguments
        ----------
            args (int): packed list, the order of arguments
            must be as follow:
            - 1st argument should be the id attribute
            - 2nd argument should be the width attribute
            - 3rd argument should be the height attribute
            - 4th argument should be the x attribute
            - 5th argument should be the y attribute
        '''
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and args[0]:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
