#include <iostream>
using namespace std;

int main()
{
const double PI = 3.1415926536;
cout << "6\" circle circumference: " << (PI * 6) << endl;

// Declare an enumerated list of constants and output some of them
enum
{RED=1, YELLOW, GREEN, BROWN, BLUE, PINK, BLACK};

cout << "I shot a red worth " << RED << endl;
cout << "Then a blue worth " << BLUE << endl;
cout << "Total scored: " << (RED + BLUE) << endl;

// Declare a custom data type and output its assigned values
typedef enum {NEGATIVE, POSITIVE} charge;
charge neutral = NEGATIVE, live = POSITIVE;
cout << "neutral wire: " << neutral << endl;
cout << "live wire: " << live << endl;

return 0;
}
