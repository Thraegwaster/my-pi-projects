# Fibonnacci Challenge
# Displays Fibonacci-like sequences using starting numbers input by the user

print("Fibonacci Sequence Calculator\n")

number1 = int(input("Enter the first number of the sequence: "))
number2 = int(input("Enter the second number of the sequence: "))
last_term = int(input("Enter the number of terms you want to be displayed: "))

print(number1)
print(number2)

# Loop to find the 3rd term onwards
counter = 2
while counter != last_term:
	total = number1 + number2
	print(total)
	number1 = number2
	number2 = total
	counter += 1

input("\n\nPress the enter key to continue")
	
