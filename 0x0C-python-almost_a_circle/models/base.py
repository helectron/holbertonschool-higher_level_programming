#!/usr/bin/python3
'''
Contain a super class
call Base
'''


class Base:
    ''' The first class is Base'''

    __nb_objects = 0  # Class attribute

    def __init__(self, id=None):  # Initializer for instantiate Base object
        '''
        Constructor
        Initializar for Base class
        '''

        if id is not None:  # If the user pass id, shall be assign
            self.id = id  # Unique instance attr, assign id with this arg value
        else:  # If there is not id, assign the counter one
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
