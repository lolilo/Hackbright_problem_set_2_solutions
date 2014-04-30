import unittest
from ps2 import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.l1 = [1, 2, 3, 4]

    def test_binary_search(self):
        self.assertEqual(binary_search(self.l1, 5), False)
        self.assertEqual(binary_search(self.l1, 4), True)

    def test_recursive_binary_search(self):
        self.assertEqual(recursive_binary_search(self.l1, 5), False)
        self.assertEqual(recursive_binary_search(self.l1, 4), True)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()