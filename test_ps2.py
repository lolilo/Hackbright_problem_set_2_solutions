import unittest
from ps2 import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.l1 = [1, 2, 3, 4]
        self.l_empty = []

    def test_binary_search(self):
        self.assertEqual(binary_search(self.l1, 5), False)
        self.assertEqual(binary_search(self.l1, 4), True)
        self.assertEqual(binary_search(self.l_empty, 9), False)

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

    def test_recursive_length_of_list(self):
        self.assertEqual(recursive_length_of_list(self.l1), 4)
        self.assertEqual(recursive_length_of_list(self.l_empty), 0)


if __name__ == '__main__':
    unittest.main()