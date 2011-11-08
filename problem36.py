# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from math import ceil

def isPalindromic(n):
	s = str(n)
	end = len(s) - 1
	for i in range(0, ceil(end / 2)):
		if s[i] != s[end - i]:
			return False
	return True

total = 0
for i in range(1, 1000000):
	b = str(bin(i))[2:]
	if isPalindromic(i) and isPalindromic(b):
		total += i

print(total)
