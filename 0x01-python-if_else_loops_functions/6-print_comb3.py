#!/usr/bin/python3
for dec in range(0, 9):
    for cent in range((dec+1), 10):
        if dec == 8 and cent == 9:
            print("{:d}{:d}".format(dec, cent))
        else:
            print("{:d}{:d}".format(dec, cent), end=", ")
