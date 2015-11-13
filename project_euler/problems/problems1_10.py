"""
`` sum_multiples_3_5`` soma valores multiplos de 3 e 5 de uma lista::

	>>> sum_values = P1(1000)
	>>> result = sum_values.sum_multiples_3_5()
	>>> print result
	233168

"""
import time
import math

class P1:

	def __init__(self, number):
		self.number = number

	def sum_multiples_3_5(self):		
		return sum([i for i in xrange(self.number) if i%3==0 or i%5==0])


class P2:

    def sum_values_fibonacci(self, max_value):
        penult, last_value = 1, 1
        soma = 0
        while last_value < max_value:
            if last_value % 2 == 0:
                soma += last_value  
            penult, last_value = last_value, last_value + penult
            
        return soma

class P3:

	def largest_value_primos_factor(self, number):
		lista = []
		largest_value = 2
		i = 2
		while True:
			if number%i == 0 and i not in lista:
				largest_value = i
				number /= i
			if number == 1:
				break
			i += 1
		return largest_value


class P4:

	def largest_palindrome_product(self):
		last_n = 999
		largest_palindrome  = 0
		for i in xrange(999, 99,-1):
			for j in xrange(last_n, 99,-1):
				if self.check_palindrome(i * j) and largest_palindrome < i*j:
					largest_palindrome = i*j
			last_n -= 1

		return largest_palindrome

	def check_palindrome(self, number):
		str_number = str(number)
		if str_number == str_number[::-1]:
			return True
		else:
			return False


class P5:

	# slow code
	def smallest_multiple(self, divisible):
		number = divisible
		cont = 0
		i = 1
		while True:
			if number%i == 0:
				cont +=1
				i +=1
			else:
				number += 2
				i = 1
				cont = 0
			if i == divisible:
				i = 1
			if cont == divisible:
				break
		return number




