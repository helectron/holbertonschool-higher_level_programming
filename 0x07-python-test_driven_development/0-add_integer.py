#!/usr/bin/python3
'''
This module is a task for the project Python Test Driven Development
for Holberton School that supplies a function to add integers.

To test run: python -m doctest -v ./tests/0-add_integer.txt
'''


def add_integer(a, b=98):
    '''A function to calculate the sum of two integer'''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a+b)
    