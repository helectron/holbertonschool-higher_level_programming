#!/usr/bin/python3
'''Module 1-my_list
Class:
    MyList (list)
'''


class MyList(list):
    '''Class for printing a list in ascending order'''

    def print_sorted(self):
        '''Prints self list in ascending order'''
        print(sorted(self))
