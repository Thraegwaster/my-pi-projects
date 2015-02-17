# Prime Factorizer
# Writes numbers as products of their prime factors

def isPrime(primecandidate):
        for i in range(2, (primecandidate // 2)):
                if primecandidate % i == 0:
                        return 0
        return primecandidate

# Gets input from user
def getInput()
	usernumber = int(input("Enter an integer:/n"))
	return usernumber

# Factorizes the number given
def factorize(usercandidate)
	index = 0 			# this is the power to which any prime factor will be raised
	quotient = usercandidate 	# this is the number we shall be left with upon division by the prime factor
	primefactor = 1 
	
	for i in range(2,usercandidate // 2):
		if isPrime(i):
			if usercandidate % i == 0:
				primefactor = i
				index = 1
				while quotient != 1:
					quotient = quotient / primefactor
					if quotient % primefactor == 0:
				 		index += 1
					else:
						break
							
