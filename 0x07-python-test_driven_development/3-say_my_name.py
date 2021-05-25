#!/usr/bin/python3
'''
This module supplies the function say_my_name().
Test it running: python3 -m doctest -v ./tests/3-say_my_name.txt
'''


def say_my_name(first_name, last_name=""):
    '''The function prints a string and two arguments'''
    print("My name is {:s} {:s}".format(first_name, last_name))