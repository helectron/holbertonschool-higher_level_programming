#!/usr/bin/python3
'''
Module 4-inherits_from
Functions:
    inherits_from(obj, a_class)
'''


def inherits_from(obj, a_class):
    '''
    Check if a object is exactly an instance of the specified class
    Arguments:
        obj: the object to evaluate
        a_class: a class to compare the object
    Return:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False
    '''
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
