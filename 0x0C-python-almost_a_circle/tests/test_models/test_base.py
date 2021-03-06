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
        self.assertEqual(bas1.id, 1)
        bas2 = Base()
        self.assertEqual(bas2.id, 2)

    def test_normal(self):
        '''Test under normal parameters'''
        bas1 = Base()
        bas2 = Base()
        bas3 = Base()
        self.assertEqual(bas1.id, (bas2.id - 1))

    def test_id(self):
        '''Test with id provided and id as None'''
        bas1 = Base(None)
        bas2 = Base(10)
        bas3 = Base()
        self.assertEqual(bas1.id, (bas3.id - 1))
        self.assertEqual(bas2.id, 10)

    def test_creating_negative(self):
        ''' Test creating a instance with a negative id '''
        b4 = Base(-10)
        self.assertEqual(b4.id, -10)

    def test_creating_float(self):
        ''' Test creating a instance with a float id '''
        b6 = Base(7.2)
        self.assertEqual(b6.id, 7.2)

if __name__ == '__main__':
    unittest.main()
