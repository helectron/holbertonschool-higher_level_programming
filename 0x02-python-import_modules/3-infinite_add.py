#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_args = len(sys.argv)
    sum = 0
    for position in range(1, n_args):
        sum = int(sys.argv[position]) + sum
    print(sum)
