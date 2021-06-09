#!/usr/bin/python3
'''
module square
Class
    Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Creates a Square object
    Properties:
        size (int): represent width and height
        from Rectangle class
        x (int): x coordenate
        y (int): y coordenate
        id (int): object identificator
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Constructor
        All parameters are set by the parent class Rectangle
        Arguments
        ---------
            size (int): represent width and height
            x (int): x coordenate
            y (int): y coordenate
            id (int): object identificator
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        overloading __str__ method that returns
        '[Square] (<id>) <x>/<y> - <size>' -
        in our case, width or height
         '''
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    # Properties
    @property
    def size(self):
        ''' Return size '''
        return self.width

    @size.setter
    def size(self, size):
        ''' Set size '''
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''
        Update the object's attributes
        Arguments
        ----------
            args (int): packed list, the order of arguments
            must be as follow:
            - 1st argument should be the id attribute
            - 2nd argument should be the size attribute
            - 3rd argument should be the x attribute
            - 4th argument should be the y attribute
        '''
        attributes = ['id', 'size', 'x', 'y']
        if args and args[0]:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''
        Returns the dictionary representation
        of the object
        '''
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
