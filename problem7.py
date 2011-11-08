# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

from sys import maxsize
from common import isPrime

primesToFind = 10001
primesFound = 0
lastPrime = 0
for n in range(2, maxsize):
	if isPrime(n):
		lastPrime = n
		primesFound += 1
		if primesFound == primesToFind:
			break

print(lastPrime)
