#!/usr/bin/python3
'''
This module supplies the function say_my_name().
Test it running: python3 -m doctest -v ./tests/3-say_my_name.txt
'''


def say_my_name(first_name, last_name=""):
    '''The function prints a string and two arguments'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
