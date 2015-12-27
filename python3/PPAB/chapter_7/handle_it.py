# Handle It
# Demonstrates handling exceptions

# try/except
try:
	num = float(input("Enter a number: "))

except ValueError:
	print("That was not a number!")
	input("\n\nPress any key to continue")
