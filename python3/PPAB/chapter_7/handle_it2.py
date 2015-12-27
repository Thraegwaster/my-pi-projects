# Handle It 2
# Handle multiple exception types

print()
for value in (None, "Hi!", 7):
	try:
		print("Attempting to convert", value, "-->", end=" ")
		print(float(value))
	except (TypeError, ValueError):
		print("Something went wrong!")

input("\n\nPress any key to continue")
