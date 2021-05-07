#!/usr/bin/python3
def no_c(my_string):
    no_more_c = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            no_more_c += letter
    return(no_more_c)
