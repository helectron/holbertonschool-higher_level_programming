#!/usr/bin/python3
'''A module that supplies one function that prints a square'''


def print_square(size):
    '''The function prints a square with the # char'''

    if not isinstance(size, int) or isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for count in range(size):
        print('#' * size)
        