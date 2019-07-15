import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """\
	
	def test_numbuses_zero(self):
        actual = a1.num_buses(0)
		expected = 0
        self.assertEqual(actual, expected)
		
	def test_numbuses_one(self):
		actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(actual, expected)
	
    def test_num_buses_1(self):
        actual = a1.num_buses(151)
        expected = 4
        self.assertEqual(actual, expected)

    def test_num_buses_2(self):
        actual = a1.num_buses(200)
        expected = 4
        self.assertEqual(actual, expected)

    def test_num_buses_3(self):
        actual = a1.num_buses(201)
        expected = 5
        self.assertEqual(actual,expected)


if __name__ == '__main__':
    unittest.main(exit=False)
