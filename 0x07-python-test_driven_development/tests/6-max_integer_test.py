#!/usr/bin/python3
"""
Unittest for max_integer
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class Documentation
    """


    def test_isEmpty(self):
        self.assertIsNone(max_integer([]))

    def test_isNotEmpty(self):
        self.assertIsNotNone(max_integer([2,4,6]))

    def test_isanInt(self):
        output = max_integer([1,2,3,4,500]))
        self.assertTrue(type(output) == int)

    def test_MaxInt(self):
        self.assertEqual(max_integer([2,2,2,23,4,5,6]), 23)
        self.assertEqual(max_integer([1,2,3,4,5,6,7,8]), 8)
        self.assertEqual(max_integer([-10, -20, -3]), -3)

    def test_isUnitary(self):
        inp_list = [1]
        self.assertEqual(max_interger(inp_list), 1)
