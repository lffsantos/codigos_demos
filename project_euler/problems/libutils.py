from math import sqrt

def check_primos_number(n):
    if n == 1 or n % 2 == 0:
        return False
    elif n <= 3:
        return True
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
		    if n % i == 0:
			    return False

	return True
