#!/usr/bin/python3
'''
Uni test for Base Class
'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Tests for Bass Class'''

    def test_create_instances(self):
        '''Test for creating instances'''
        bas1 = Base()
        self.assertEqual(b1.id, 1)
        bas2 = Base()
        self.assertEqual(b2.id, 2)

    def test_normal(self):
        '''Test under normal parameters'''
        bas1 = Base()
        bas2 = Base()
        bas3 = Base()
        self.assertEqual(bas1.id, (bas2.id - 1))

if __name__ == '__main__':
    unittest.main()
