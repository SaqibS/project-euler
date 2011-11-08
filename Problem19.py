# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def isLeapYear(year):
	if year % 4 != 0:
		return False
	if year % 100 == 0 and year % 400 != 0:
		return False
	return True

daysInMonth = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }

def getNextSunday(year, month, day):
	if month == 2:
		daysInMonth[2] = 29 if isLeapYear(year) else 28

	day += 7
	if day > daysInMonth[month]:
		day -= daysInMonth[month]
		month += 1
		if month > 12:
			month = 1
			year += 1

	return (year, month, day)

# Start with a Sunday that we know about:
currentYear = 1899
currentMonth = 12
currentDay = 31

# Search bounds:
startYear = 1901
endYear = 2000

# Find the first Sunday in the millennium:
while currentYear < startYear:
	(currentYear,currentMonth,currentDay) = getNextSunday(currentYear, currentMonth, currentDay)

# Find all the rest of the Sundays in the millennium:
numSundaysOnFirstOfMonth = 0
while currentYear <= endYear:
	if currentDay == 1:
		numSundaysOnFirstOfMonth += 1
	(currentYear,currentMonth,currentDay) = getNextSunday(currentYear, currentMonth, currentDay)

print(numSundaysOnFirstOfMonth)
