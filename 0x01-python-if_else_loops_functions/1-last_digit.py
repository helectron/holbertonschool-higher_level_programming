#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
        num = number % -10
elif number >= 0:
        num = number % 10
if num > 5:
    print('Last digit of {:d} is {:d} '
          'and is greater than 5\n'.format(number, num))
elif num == 0:
    print('Last digit of {:d} is {:d} '
          'and is 0\n'.format(number, num))
elif num < 6:
    print('Last digit of {:d} is {:d} '
          'and is less than 6 and not 0\n'.format(number, num))
