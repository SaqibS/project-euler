# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isPythagoreanTriplet(a, b, c):
	return a**2 + b**2 == c**2

def findPythagoreanTripletTotaling(n):
	for a in range(1, n):
		for b in range(1, n-a):
			c = n - b - a
			if isPythagoreanTriplet(a, b, c):
				return (a, b, c)

tripplet = findPythagoreanTripletTotaling(1000)
product = 1
for x in tripplet:
	product *= x

print(product)
