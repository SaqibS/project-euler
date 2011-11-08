# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

def equalToSumOfFactorialOfDigits(n):
	return n == sum([factorial(int(x)) for x in str(n)])

print(sum([x for x in range(3, 1000000) if equalToSumOfFactorialOfDigits(x)]))
