# n! means n * (n - 1) * ... * 3 * 2 * 1
# Find the sum of the digits in the number 100!

from math import factorial

print(sum([int(c) for c in str(factorial(100))]))
