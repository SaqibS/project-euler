# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

from math import floor

mappings = { 0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", \
10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", \
20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety" }

def numberToString(n):
	if n == 1000:
		return "one thousand"

	hundreds = int(floor(n / 100))
	tens = int(floor((n % 100) / 10))
	units = n % 10

	s = ""
	if hundreds > 0:
		s += mappings[hundreds] + " hundred"
	if hundreds > 0 and (tens > 0 or units > 0):
		s += " and "
	if 10 * tens + units < 20:
		s += mappings[10 * tens + units]
	else:
		if tens > 0:
			s += mappings[10 * tens]
		if tens > 0 and units > 0:
			s += "-"
		if units > 0:
			s += mappings[units]
	return s

print(sum([len(numberToString(i).replace(" ", "").replace("-", "")) for i in range(1, 1001)]))
