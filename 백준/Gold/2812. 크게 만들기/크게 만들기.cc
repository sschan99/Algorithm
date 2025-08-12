#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, K;
	cin >> N >> K;

	char num, *stack = new char[N];

	int idx = -1, nullIdx = N - K;

	for (int _ = 0; _ < N; _++) {
		cin >> num;
		while (K > 0 && idx >= 0 && stack[idx] < num) {
			--K;
			--idx;
		}
		stack[++idx] = num;
	}
	stack[nullIdx] = '\0';
	
	cout << stack;
	delete[] stack;
	return 0;
}
