# Fibonacci
# Prints out the Fibonacci sequence to a user-specified length

def fibonacci(sequence_length):
	"Return the Fibonacci sequence of length *sequence_length*"
	sequence = [0,1]
	if sequence_length < 1:
		print("Fibonacci sequence only defined for length 1 or greater")
		return
	if 0 < sequence_length < 3:
		return sequence[:sequence_length]
	for i in range(2,sequence_length):
		sequence.append(sequence[i-1]+sequence[i-2])
	return sequence

requested_length = int(input("What length of Fibonacci sequence would you like?: "))

print(fibonacci(requested_length))

input("\n\nPress the enter key to exit.")
