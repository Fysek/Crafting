import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """
	def test_stock_price_summary_empty(self):
        actual = a1.stock_price_summary([])
		expected = (0, 0)
        self.assertEqual(actual, expected)
			
	def test_stock_price_summary_onezero(self):
        expected = (0, 0)
        actual = a1.stock_price_summary([0.0])
        self.assertEqual(actual, expected)		
		
	def test_stock_price_summary_onepositive(self):
        actual = a1.stock_price_summary([1.2])
		expected = (1.2, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_onenegative(self):
        actual = a1.stock_price_summary([-1.2])
		expected = (0, -1.2)
        self.assertEqual(actual, expected)	
			
    def test_stock_price_summary_1(self):
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_2(self):
        actual = a1.stock_price_summary([0.10, 0.04, 0.05, 0.52, 0, 0.62, 0.01])
        expected = (1.34, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_3(self):
        actual = a1.stock_price_summary([-0.10, -0.04, -0.05, -0.52, 0, -0.62, -0.01])
        expected = (0, -1.34)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
