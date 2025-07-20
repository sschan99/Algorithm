#include <iostream>
#include <vector>

using namespace std;

long det(int a, int b, int c, int d)
{
	return 1L * a * d - 1L * b * c;
}

int main() {
	int N;
	cin >> N;

	vector<int> height(N);
	for (int &x : height) cin >> x;

	int max = 0;

	for (int point = 0; point < N; ++point)
	{
		int a, b, count = 0;

		a = 0, b = -1;
		for (int i = point + 1; i < N; ++i)
		{
			int c = i - point, d = height[i] - height[point];
			if (det(a, b, c, d) > 0)
			{
				++count;
				a = c, b = d;
			}
		}

		a = 0, b = -1;
		for (int i = point - 1; i >= 0; --i)
		{
			int c = i - point, d = height[i] - height[point];
			if (det(a, b, c, d) < 0)
			{
				++count;
				a = c, b = d;
			}
		}

		if (max < count) max = count;
	}

	cout << max;

	return 0;
}
