# Divider
# Takes a number and a divisor as input, then counts how many times
# the number goes into the divisor before a remainder is enocuntered.

def divider(dividend, divisor):
	
	index = 0
	
	# we don't want dividend to be changed by the subsequent calculation.
	quotient = dividend
	while quotient % divisor == 0:
		quotient = quotient / divisor
		index += 1
	
	return index

# main
userdividend = int(input("Enter the dividend\n"))
userdivisor = int(input("Enter the divisor\n"))

answer = divider(userdividend, userdivisor)

print("\nThere is a factor of", userdivisor, "^", answer, "in", userdividend, ".")

input("\n\nPress the enter key to continue")
