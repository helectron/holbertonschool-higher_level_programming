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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns the JSON string representation
        of `list_dictionaries`
        Arguments
        ---------
            list_dictionaries (list): list of dictionaries
        '''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Wite json in a new file'''

        if list_objs is None:
            new_list = []
        else:
            new_list = []
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open("{}.json".format(cls.__name__), "w") as write_file:
            write_file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returnes the list of JSON string
        representation `json_string`
        Arguments:
            json_string (str): string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        
        return json.loads(json_string)
