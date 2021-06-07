#!/usr/bin/python3
''' 0-main '''


class Base:

    __nb_objects = 0  # Class attribute

    def __init__(self, id=None):  # Initializer for instantiate Base object
        if id is not None:  # If the user pass id, shall be assign
            self.id = id  # Unique instance attribute, assign id with this argument value
        else:  # If there is not id, assign the counter one
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
