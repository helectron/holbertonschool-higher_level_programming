#!/usr/bin/python3
'''module 5-save_to_json_file
Functions:
    save_to_json_file(my_obj, filename)'''
import json


def save_to_json_file(my_obj, filename):
    '''Saves an object in json representation'''
    with open(filename, "w") as json_file:
        json_file.write(json.dumps(my_obj))
    json_file.close()
