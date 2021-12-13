import math_operations
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function math_operations.swap_k. """
    
    def test_swap_k_empty(self):
        list_1 = []
        math_operations.swap_k(list_1, 0)
        expected = []
        self.assertEqual(list_1, expected)
		
    def test_swap_k_oneitem(self):
        list_1 = [1]
        expected = [1]
        math_operations.swap_k(list_1, 0)
        self.assertEqual(list_1, expected)		
		
    def test_swap_k_1(self):
        actual = math_operations.swap_k([12, 23, 15, 34, 67, 6, 7, 8, 45, 31], 3)
        expected = [31, 45, 8, 34, 67, 6, 7, 15, 23, 12]
        self.assertEqual(actual, expected)

    def test_swap_k_2(self):
        actual = math_operations.swap_k([10, 33, 46, 15, 34, 34, 12, 42, 45, 31], 0)
        expected = [10, 33, 46, 15, 34, 34, 12, 42, 45, 31]
        self.assertEqual(actual, expected)

    def test_swap_k_3(self):
        actual = math_operations.swap_k([42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42], 2)
        expected = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
