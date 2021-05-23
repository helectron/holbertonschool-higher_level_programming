#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for lists in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(lists, a_dictionary[lists]))
