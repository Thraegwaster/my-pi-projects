# Random Access
# Demonstrates string indexing

import random

word = input("Enter your word: ")
print("The word is: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
	position = random.randrange(low, high)
	print("word[", position, "]\t", word[position])

input("Press the enter key to exit.")
