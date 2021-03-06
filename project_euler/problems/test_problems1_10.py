'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
import unittest
from problems1_10 import P1, P2, P3, P4, P5, P6, P7, P8

class TestEuller(unittest.TestCase):

	def test_sum_multiples_3_5(self):
		pro_1 = P1(1000)
		sum_values = pro_1.sum_multiples_3_5()
		self.assertEqual(233168,sum_values)

	def test_fibonnaci(self):
		pro2 = P2()
		sum_values = pro2.sum_values_fibonacci(4000000)
		self.assertEqual(4613732,sum_values)

	def test_primos_factor(self):
		pro3 = P3()
		largest_prime_factor = pro3.largest_value_primos_factor(600851475143)
		self.assertEqual(6857,largest_prime_factor)

	def test_largest_palindrome_product(self):
		pro4 = P4() 
		largest_palindrome_product = pro4.largest_palindrome_product()
		self.assertEqual(906609,largest_palindrome_product)


	def test_smallest_multiple(self):
		pro5 = P5()
		smallest_multiple = pro5.smallest_multiple(10)
		self.assertEqual(2520,smallest_multiple)

	def test_sum_square_difference(self):
		pro6 = P6()
		sum_square_difference = pro6.sum_square_difference(100)
		self.assertEqual(25164150,sum_square_difference)		

	def test_value_n_prime(self):
		pro7 = P7()
		value_n_prime = pro7.value_n_prime(10001)
		self.assertEqual(104743,value_n_prime)		

	def test_largest_product_in_serie(self):
		pro8 = P8()
		largest_product_in_serie = pro8.largest_product_in_serie(13)
		self.assertEqual(23514624000,largest_product_in_serie)			


if __name__ == '__main__':
    unittest.main()
