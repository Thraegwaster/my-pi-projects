# No Vowels
# Demonstrates creating new strings with a for loop

message = input("Enter a message: ")
clue = input("Enter your clue: ")

def clear(num):
	for i in range(num):
		print(" ") 

clear(80)

new_message = ""
VOWELS ="aeiou"

print()
for letter in message:
	if letter.lower() not in VOWELS:
		new_message += letter
		# print("A new string has been created:", new_message)

print("\nThe phrase without vowels is:", new_message)
print("\nYour clue is:", clue)

input("\n\nPress the enter key to exit.")
