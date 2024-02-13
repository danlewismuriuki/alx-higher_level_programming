import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor_with_id(self):
        """ Test constructor with id argument """
        rect = Rectangle(10, 20, 5, 6, id=1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 6)

    def test_constructor_without_id(self):
        """ Test constructor without id argument """
        rect = Rectangle(15, 25, 7, 8)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 8)

    def test_getters_and_setters(self):
        """ Test getters and setters """
        rect = Rectangle(20, 30, 10, 12)

        rect.width = 25
        rect.height = 35
        rect.x = 15
        rect.y = 18

        self.assertEqual(rect.width, 25)
        self.assertEqual(rect.height, 35)
        self.assertEqual(rect.x, 15)
        self.assertEqual(rect.y, 18)

    def test_invalid_value(self):
        """ Test seting invalid values """
        rect = rectangle(10, 20)
        with self.assertRaises(ValueError):
            rect.width = -5
        with self.assertRaises(ValueError):
            rect.height = "invalid"
        with self.assertRaises(ValueError):
            rect.x = [1, 2, 3]
        with self.assertRaises(ValueError):
            rect.y = None

  if __name__ == '__main__':
      unittest.main()
