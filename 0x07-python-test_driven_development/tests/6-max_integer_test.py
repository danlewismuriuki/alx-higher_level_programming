#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_case_2(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_case_3(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_case_4(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_case_5(self):
        self.assertEqual(max_integer([4, 2, 3, -1]), 4)

    def test_case_6(self):
        self.assertEqual(max_integer([-4, -13, -12, -11]), -4)

    def test_case_7(self):
        self.assertEqual(max_integer([4]), 4)

    def test_case_8(self):
        self.assertIsNone(max_integer([]))
