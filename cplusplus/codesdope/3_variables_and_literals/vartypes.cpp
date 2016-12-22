#include <iostream>

int main()
{
	using namespace std;
	int i; 		// integer variable declaration
	float f; 	// floating point variable
	double d;	// double variable
	char c;		// character variable
	bool b, bl;	// boolean variable

	// assigning values to these variables

	i = 45;
	f = 34.234;
	d = 34.43243343;
	c = 'g';
	b = true;
	bl = 5 < 4;

	cout << "int : " << i << endl;
	cout << "float : " << f << endl;
	cout << "double : " << d << endl;
	cout << "char : " << c << endl;
	cout << "b : " << b << endl;
	cout << "bl : " << bl << endl;

	return 0;
}
