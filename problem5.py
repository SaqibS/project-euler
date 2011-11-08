# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import factorial

def isDivisibleByAllNumbersInRange(val, min, max):
	for n in range(max, min-1, -1):
		if val % n != 0:
			return False
	return True

min = 2 # All numbers are divisible by 1
max = 20
for n in range(max, factorial(max)+1, max):
	if isDivisibleByAllNumbersInRange(n, min, max):
		print(n)
		break
