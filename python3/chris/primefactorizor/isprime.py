# IsPrime
# Determines whether a given integer is prime

def isPrime(primecandidate):
	for i in range(2, (primecandidate // 2)):
		if primecandidate % i == 0:
			return 0
	return primecandidate

# main
mycand = int(input("Enter the prime candidate: "))
if isPrime(mycand) == 0:
	print(mycand, "is not prime")
else:
	print(mycand, "is a prime number")

input("\n\nPress the enter key to continue")


		
