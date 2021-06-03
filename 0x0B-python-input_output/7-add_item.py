#!/usr/bin/python3
'''
module 7-add_item
Adds all arguments to a Python list, and then save them to a file:
'''
import sys

# load functions
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
# load json or create a new list
try:
    file = load_from_json_file("add_item.json")
except FileNotFoundError:
    file = list()
# read arguments from stdin
for x in sys.argv[1:]:
    file.append(x)
save_to_json_file(file, "add_item.json")