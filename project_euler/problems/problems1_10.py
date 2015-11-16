"""
`` sum_multiples_3_5`` soma valores multiplos de 3 e 5 de uma lista::

	>>> sum_values = P1(1000)
	>>> result = sum_values.sum_multiples_3_5()
	>>> print result
	233168

"""

from libutils import check_primos_number

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

class P6:

	def sum_square_difference(self, max_value):
		soma_1, soma_2 = 0, 0 
		for i in xrange(max_value+1):
			soma_1 += pow(i, 2)
			soma_2 += i
		soma_2 = pow(soma_2,2)
		diff = soma_2 - soma_1
		return diff 

class P7:

	def value_n_prime(self, position):
		cont = 1
		number = 1
		while True:
			if check_primos_number(number):
				cont +=1
				if cont == position:
					break
			number +=2

			
		return number

class P8:

	def __init__(self):
		self.serie = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

	def largest_product_in_serie(self, number):
		serie_list = []
		i = 0
		max_product = 0
		for s in self.serie:
			serie_list.append(s)
			i+=1
			if len(serie_list) > number-1:
				temp_product = eval('*'.join(serie_list[i-number:i]))
				if max_product < temp_product:
					max_product = temp_product
		
		return max_product






