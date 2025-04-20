#include <iostream>
#include <string>
using namespace std;

int main()
{
	string L1, L2, L3;
	cin >> L1 >> L2 >> L3;

	int next;
	if (isdigit(L1[0]))
	{
		next = stoi(L1) + 3;
	}
	else if (isdigit(L2[0]))
	{
		next = stoi(L2) + 2;
	}
	else
	{
		next = stoi(L3) + 1;
	}

	if (next % 3 != 0 && next % 5 != 0)
	{
		cout << next;
		return 0;
	}
	if (next % 3 == 0)
	{
		cout << "Fizz";
	}
	if (next % 5 == 0)
	{
		cout << "Buzz";
	}
}