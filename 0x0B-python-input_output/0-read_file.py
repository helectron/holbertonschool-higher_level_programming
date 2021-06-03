#!/usr/bin/python3
'''module 0-read_file
Functions:
    read_file(filename="")
'''


def read_file(filename=""):
    '''read to stdout text from a file
    Arguments:
        filename: string with file's path
    '''
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
    myFile.close()
