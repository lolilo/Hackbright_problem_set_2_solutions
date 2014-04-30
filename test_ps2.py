import unittest
from ps2 import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.l1 = [1, 2, 3, 4]

    def test_binary_search(self):
        self.assertEqual(binary_search(self.l1, 5), False)
        self.assertEqual(binary_search(self.l1, 4), True)

if __name__ == '__main__':
    unittest.main()