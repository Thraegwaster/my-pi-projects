# Maitre D'
# Demonstrates treating a value as a condition

print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many pounds do you slip the Maitre D'? "))

# The if statement below is equivalent to "if money != 0:"
if money:
	print("Ah, I am reminded of a table. Please come this way.")
else:
	print("Please, sit. It may be a while.")

input("\n\nPress the enter key to exit.")
