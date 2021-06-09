#!/usr/bin/python3
'''
module base
Class
    Base
'''
import json


class Base:
    '''
    Manage 'id' attribute in all furture instances of this class
    and to avoid duplicating the same code (by extension, same bugs)
    Class Attributes
    ----------------
        __nb_objects (int): number of instances from Base class
    Methods
    -------
        __init__(self, id=None)
        '''

    __nb_objects = 0  # Class attribute

    def __init__(self, id=None):  # Initializer for instantiate Base object
        '''
        Constructor
        if 'id' is set to 'None' the '__nb_objects' is
        incremented by one and set as the id for the new object
        Arguments
        ---------
            id (int): id number for the new object
        '''

        if id is not None:  # If the user pass id, shall be assign
            self.id = id  # Unique instance attr, assign id with this arg value
        else:  # If there is not id, assign the counter one
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# Static method
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return '[]'
        else:
            return list_dictionaries
