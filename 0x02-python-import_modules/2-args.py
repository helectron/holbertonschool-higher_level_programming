#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_args = len(sys.argv)
    if n_args == 1:
        print('{}'.format('0 arguments.'))
    if n_args == 2:
        print('{}'.format('1 argument.'))
    if n_args > 2:
        print('{:d} arguments:'.format(n_args - 1))
    for position in range(1, n_args):
        print('{:d}: {:s}'.format(position, sys.argv[position]))
