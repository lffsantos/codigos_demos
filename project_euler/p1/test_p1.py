'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
import unittest
from p1 import P1

class TestHiker(unittest.TestCase):

	def test_sum_multiples_3_5(self):
		pro_1 = P1(1000)
		sum_values = pro_1.sum_multiples_3_5()
		self.assertEqual(466335,sum_values)

if __name__ == '__main__':
    unittest.main()
