"""
`` sum_multiples_3_5`` soma valores multiplos de 3 e 5 de uma lista::

	>>> sum_values = P1(1000)
	>>> result = sum_values.sum_multiples_3_5()
	>>> print result
	233168

"""
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