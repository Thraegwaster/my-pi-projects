# Random number generator
#
# This is just for testing purposes

# Imports
import random

# Now generate and print random integers from 1 to 100

try:
	counter = 1
	int_holder = []
	for counter in range(1,100,1):
		myNum = random.randint(1,100)
		int_holder.append(myNum)
	print(int_holder)

except KeyboardInterrupt:
	print("Finishing Random Number Program")
