'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
import unittest
from problems1_10 import P1, P2

class TestEuller(unittest.TestCase):

	# Teste Problem 1
	def test_sum_multiples_3_5(self):
		pro_1 = P1(1000)
		sum_values = pro_1.sum_multiples_3_5()
		self.assertEqual(233168,sum_values)

	def test_fibonnaci(self):
		pro2 = P2()
		sum_values = pro2.sum_values_fibonacci(4000000)
		self.assertEqual(4613732,sum_values)

if __name__ == '__main__':
    unittest.main()
