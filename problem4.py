# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
	return str(n) == str(n)[::-1]

largestPalindrome = 0
for i in range(999, 99, -1):
	for j in range(i, 99, -1):
		product = i * j
		if isPalindrome(product) and product > largestPalindrome:
			largestPalindrome = product
			break
print(largestPalindrome)
