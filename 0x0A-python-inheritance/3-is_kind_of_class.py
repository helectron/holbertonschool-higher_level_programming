#!/usr/bin/python3
'''Module 3-is_kind_of_class
Functions:
    is_kind_of_class(obj, a_class)
'''


def is_kind_of_class(obj, a_class):
    '''Check if the object is an instance of, or if the object
       is an instance of a class that inherited from, the specified class

    Arguments:
        obj: the object to evaluate
        a_class: the class to compare the object

    Return:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class. Otherwise False
    '''
    return type(obj, a_class)
