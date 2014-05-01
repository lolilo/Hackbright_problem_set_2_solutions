import unittest
from ps2 import *

class TestProblemSet2Functions(unittest.TestCase):

    def setUp(self):
        self.l1 = [1, 2, 3, 4]
        self.l_empty = []
        self.l2 = [5, 9, 1, 3, 7, 6, 2]
        self.l3 = [2, 3, 1]

    def test_binary_search(self):
        self.assertEqual(binary_search(self.l1, 5), False)
        self.assertEqual(binary_search(self.l1, 4), True)
        self.assertEqual(binary_search(self.l_empty, 9), False)

    def test_binary_search_better(self):
        self.assertEqual(binary_search_better(self.l1, 5), False)
        self.assertEqual(binary_search_better(self.l1, 4), True)
        self.assertEqual(binary_search_better(self.l_empty, 9), False)

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

    def test_quick_sort_one_pass(self):
        self.assertEqual(quick_sort_one_pass([5, 9, 1, 3, 7, 6, 2]), [3, 2, 1, 5, 7, 6, 9])
        self.assertEqual(quick_sort_one_pass([2, 3, 1]), [1, 2, 3])

    def test_tuples_that_add_to_target(self):
        self.assertEqual(tuples_that_add_to_target([1, 2, 3, 4, 0], 3), [(0,3), (1,2)])
        self.assertEqual(tuples_that_add_to_target([0, 0, -1, 1, 0, 1, -1], 0 ), [(0, 0), (1, -1), (1, -1)])

if __name__ == '__main__':
    unittest.main()