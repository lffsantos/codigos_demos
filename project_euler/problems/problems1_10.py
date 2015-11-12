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

	def primos_factor(self, number):
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



