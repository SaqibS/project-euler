# Pentagonal numbers are generated by the formula, P_n=n(3n-1)/2. The first ten pentagonal numbers are:
#  1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#  It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference, 70 - 22 = 48, is not pentagonal.
#  Find the pair of pentagonal numbers, P_j and P_k, for which their sum and difference is pentagonal and D = |P_k - P_j| is minimised; what is the value of D?

from math import sqrt, floor

def isPentagonal(x):
	n = (sqrt(24 * x + 1) + 1) / 6
	return n - floor(n) == 0

pentagonals = [1]
for n in range(2, 1000000):
	x = int(n * (3 * n - 1) / 2)
	for y in pentagonals:
		if isPentagonal(x + y) and isPentagonal(abs(x - y)):
			print(abs(x - y))
			exit()
	pentagonals.append(x)