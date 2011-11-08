# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from common import isPrime

print(2 + sum([n for n in range(3, 2000000+1, 2) if isPrime(n)]))
