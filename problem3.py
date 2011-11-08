# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from math import sqrt
from common import isPrime

val = 600851475143
if isPrime(val):
	print(val)
	exit()
for n in range(int(sqrt(val))+1, 0, -1):
	if val % n == 0 and isPrime(n):
		print(n)
		break
