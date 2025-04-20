#include <iostream>
using namespace std;

int main()
{
	int n, t, p;
	int size[6]{};
	cin >> n;
	for (int i = 0; i < 6; i++)
	{
		cin >> size[i];
	}
	cin >> t >> p;

	int result = 0;
	for (int i = 0; i < 6; i++)
	{
		result += (size[i] + t - 1) / t;
	}
	cout << result << endl;
	cout << n / p << ' ' << n % p << endl;
}