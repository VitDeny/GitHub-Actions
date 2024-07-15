import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import add, subtract, multiply, divide

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(10, 2), 12)
        self.assertEqual(add(4, 5), 9)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(3, 3), 9)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(12, 3), 4)
        self.assertEqual(divide(15, 5), 3)

if __name__ == "__main__":
    unittest.main()
