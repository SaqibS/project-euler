# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from math import floor, sqrt

def is9Pandigital(x, y, z):
	s = str(x) + str(y) + str(z)
	return len(s) == 9 and "".join(sorted(list(s))) == "123456789"

products = []
for z in range(1, floor(sqrt(123456789)) + 1):
	for y in range(1, floor(sqrt(z)) + 1):
		if z % y == 0:
			x = int(z / y)
			if is9Pandigital(x, y, z) and not z in products:
				products.append(z)

print(sum(products))
