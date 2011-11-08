# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

from common import isPrime

def isCircularPrime(n):
	s = str(n)
	for i in range(len(s)):
		if not isPrime(int(s)):
			return False
		s = s[1:] + s[0]
	return True

print(len([x for x in range(1, 1000000) if isCircularPrime(x)]))
