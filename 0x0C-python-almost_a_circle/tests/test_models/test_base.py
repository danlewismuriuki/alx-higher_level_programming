import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        """ Test constructor with id argument """
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)

    def test_init_without_id(self):
        """ Test constructor without id """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

    def test_incrementing_id(self):
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance.id, 1)
        self.assertEqual(base_instance.id, 2)
