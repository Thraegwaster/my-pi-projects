// PrimeLister.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cmath> /* pow and llround */


bool checkNumberValid(long primecand)
{
	// Checks whether the prime candidate the user has entered is within the range of integers C++ can handle.
	// first find the size of a long integer:
	double longMax;
	longMax = llround(pow(2,sizeof(long)*8)); // There are 8 bits in a byte
	std::cout << longMax << std::endl;
	
	// long llongMax = static_cast<long>(longMax); // Static cast to change output of power function above back to an integer

	if (primecand < longMax && primecand > 1)
		return true;

	return false;

}

bool anotherGo()
{
	using namespace std;
	cout << endl << "Would you like to try another number? (y/n): ";
	char answer;
	cin >> answer;
	if (answer == 'y' || answer == 'Y')
		return true;
	else
		return false;

}

bool isPrime(unsigned long long primecand)
{
	// First, check whether the prime candidate (primecand) is divisible by 2
	if (primecand % 2 == 0 && primecand != 2)
		return false;
	for (unsigned long long count = 3; count < (primecand / 2) + 1; count = count + 2)
		if (primecand % count == 0)
			return false;
	return true;
}

long numberPrimes()
{
	using namespace std;
	cout << "How many primes would you like to find? ";

	/* Don't know whether the variable below should be an unsigned long - next step? */
	long primesToCount;
	cin >> primesToCount;
	if (checkNumberValid(primesToCount) == false)
	{
		cout << endl << "The number of primes must be between 1 and 4,294,967,295" << endl;
		numberPrimes();
	}
	return primesToCount;
}

long findPrimes(long primesToCount)
{
	using namespace std;
	long count = 1;
	long primesFound = 0;
	while (primesFound < primesToCount)
	{
		if (isPrime(count))
		{
			cout << primesFound + 1 << "\t" << count << endl;
			primesFound++;
		}
		count++;
	}
		
	return 0;

}


int main()
{
	using namespace std;
restartpoint:

	// Get input from user
	
	long primesToCount;
	primesToCount = numberPrimes();

	findPrimes(primesToCount);
	if (anotherGo() == true)
		goto restartpoint;
	return 0;
} 
