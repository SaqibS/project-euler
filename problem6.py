# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares(min, max):
	return sum([n**2 for n in range(min, max+1)])

def squareOfSum(min, max):
	return sum(range(min, max+1))**2

min = 1
max = 100
difference = sumOfSquares(min, max) - squareOfSum(min, max)
if difference < 0:
	difference *= -1

print(difference)
