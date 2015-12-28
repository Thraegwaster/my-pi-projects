# Handle It 2
# Handle multiple exception types

print()
for value in (None, "Hi!", 7):
    try:
        print("Attempting to convert", value, "-->", end=" ")
	print(float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError:
        print("I can only convert a string of digits!")

input("\n\nPress any key to continue")
