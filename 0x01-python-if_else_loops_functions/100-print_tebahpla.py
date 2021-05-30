#!/usr/bin/python3

for x in range(122, 96, -1):
    if x % 2 == 0:
        character = chr(x)
    else:
        character = chr(x - 32)
    print("{}".format(character), end='')
