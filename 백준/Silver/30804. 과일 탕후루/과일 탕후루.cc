#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int N;
	cin >> N;

	vector<int> S;
	S.reserve(N);

	for (int i = 0; i < N; i++)
	{
		int x;
		cin >> x;
		S.push_back(x);
	}

	vector<int>::iterator front = S.begin(), back = S.begin();
	int fruits[10]{};
	int count = 0;

	while (back != S.end())
	{
		if (fruits[*back]++ == 0)
		{
			count++;
		}
		back++;
		
		if (count <= 2)
		{
			continue;
		}

		if (--fruits[*front] == 0)
		{
			count--;
		}
		front++;
	}
	cout << back - front;
}