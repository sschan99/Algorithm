#include <iostream>
#include <string>
using namespace std;

int main()
{
	int target = 0;
	for (int i = 0; i < 3; i++)
	{
		string line;
		cin >> line;
		if (isdigit(line[0]))
		{
			target = stoi(line) + 3 - i;
			break;
		}
	}

	if (target % 3 != 0 && target % 5 != 0)
	{
		cout << target;
		return 0;
	}
	if (target % 3 == 0)
	{
		cout << "Fizz";
	}
	if (target % 5 == 0)
	{
		cout << "Buzz";
	}
}