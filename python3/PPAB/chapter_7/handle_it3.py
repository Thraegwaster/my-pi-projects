# Handle It 3
# Getting an exception's argument.

try:
	num = float(input("\nEnter a number: "))
	print("Your number was", num)

except ValueError as e:
	print("That was not a number! Python says it", e)
