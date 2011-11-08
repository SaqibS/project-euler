# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
 # Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
 # NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from common import isPrime

def isTruncatablePrime(n, leftToRight):
	s = str(n)
	while len(s) > 0:
		if not isPrime(int(s)):
			return False
		s = s[1:] if leftToRight else s[:-1]
	return True

print(sum([x for x in range(10, 1000000) if isTruncatablePrime(x, True) and isTruncatablePrime(x, False) and len(locals()) < 11]))
