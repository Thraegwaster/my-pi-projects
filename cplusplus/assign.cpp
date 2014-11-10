#include <iostream>
using namespace std;

int main()
{
int a, b;

cout << "Assign values: ";
cout << "a = " << (a = 8) << " ";
cout << "b = " << (b = 4);

// Statements to output combined assigned values
cout << endl << "Add and assign: ";
cout << "a += b (8 += 4) a = " << (a += b);
cout << endl << "Subtract and assign: ";
cout << "a -= b (12 -= 4) a = " << (a -= b);
cout << endl << "Multiply and assign: ";
cout << "a *= b (8 *= 4) a = " << (a *= b);
cout << endl << "Divide and assign: ";
cout << "a /= b (32 /= 4) a = " << (a /= b);
cout << endl << "Modulus and assign: ";
cout << "a %= b (12 %= 4) a = " << (a %= b) << endl;
 
return 0;
}
