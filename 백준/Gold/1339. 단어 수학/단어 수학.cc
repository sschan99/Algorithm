#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solve() {
	int N;
	cin >> N;

	vector<int> counter(26, 0);

	while (N--) {
		string word;
		cin >> word;

		int x = 1;
		for (auto iter = word.rbegin(); iter != word.rend(); iter++) {
			counter[*iter - 'A'] += x;
			x *= 10;
		}
	}

	int result = 0;
	for (int i = 9; i >= 0; i--) {
		auto maxIter = max_element(counter.begin(), counter.end());
		result += *maxIter * i;
		*maxIter = 0;
	}
	return result;
}

int main() {
	cout << solve();
	return 0;
}
