#include <iostream>
using namespace std;

bool anotherGo()
{
	char response;
	cout << "Another go? (Y/N)? : ";
	cin >> response;
	if(response == 'y' || 'Y')
	{
		return true;
	}
	else
		return false;
}
int main()
{
	char ch;
	cout << "enter a single character: ";
	cin >> ch;
	cout << "The ASCII code for your character is " << int(ch) << endl;
	anotherGo();
	return 0;
} 
