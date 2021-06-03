#!/usr/bin/python3
'''module 2-append_write
Function:
    append_write(filename="", text="")
'''


def append_write(filename="", text=""):
    '''Function to append a text in a file'''
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
