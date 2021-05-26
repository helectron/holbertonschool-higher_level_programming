#!/usr/bin/python3
'''
A module that supplues one function: text_identation().

To test, run: `python3 -m doctest ./tests/5-text_indentation.txt`
'''


def text_indentation(text):
    ''' 
    prints to stdout text with 2 new lines after certain characters
    Arguments:
    text: must be a string
    '''
    if type(text) is not str or len(text) < 0:
        raise TypeError("text must be a string")
    # replace chars with placeholder
    text = text.replace('.', '.\n\n')
    # print(text)
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print(text, end='')