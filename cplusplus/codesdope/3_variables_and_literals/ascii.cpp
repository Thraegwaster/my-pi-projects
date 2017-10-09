#include <iostream>
using namespace std;

bool anotherGo()
{
	char response;
	cout << "Another go? (Y/N)? : ";
	cin >> response;
	if(response == 'y')
	{
		return true;
	}
	else
		return false;
}
int main()
{
	restartpoint:
	char ch;
	cout << "enter a single character: ";
	cin >> ch;
	cout << "The ASCII code for your character is " << int(ch) << endl;
	if(anotherGo() == true)
	{
		goto restartpoint;
	}
	else return 0;
} 
