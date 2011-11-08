# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

def isTriangleNumber(num):
	for n in range(1, num+1):
		if 0.5 * n * (n + 1) == num:
			return True
	return False

def wordValue(word):
	return sum([ord(c) - 64 for c in word])

def isTriangleWord(word):
	return isTriangleNumber(wordValue(word))

file = open("words.txt", "r")
words = [x.strip('"') for x in file.read().split(",")]
print(len([word for word in words if isTriangleWord(word)]))
file.close()
