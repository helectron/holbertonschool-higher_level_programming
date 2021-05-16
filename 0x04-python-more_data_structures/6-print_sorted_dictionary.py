#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for lists in sorted(my_dict.keys()):
        print("{:s}: {}".format(lists, my_dict[lists]))
