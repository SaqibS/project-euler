from math import sqrt, ceil

def isPrime(n):
	if n == 2:
		return True
	if n < 2 or (n > 2 and n % 2 == 0):
		return False
	for i in range(3, int(sqrt(n))+1, 2):
		if n % i == 0:
			return False
	return True

def sumOfProperDivisors(n):
	return sum([i for i in range(1, ceil(n/2)+1) if n%i == 0])
