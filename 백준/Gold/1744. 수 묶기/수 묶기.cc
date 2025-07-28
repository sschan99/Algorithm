#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
	int N, x, result = 0;
	cin >> N;
	
	vector<int> greaterThan1, lessThan1;
	for (int i = 0; i < N; i++) {
		cin >> x;
		if (x > 1) greaterThan1.push_back(x);
		else if (x < 1) lessThan1.push_back(x);
		else result++;
	}
	sort(greaterThan1.rbegin(), greaterThan1.rend());
	sort(lessThan1.begin(), lessThan1.end());

	if (greaterThan1.size() % 2 == 1) {
		result += greaterThan1.back();
		greaterThan1.pop_back();
	}
	if (lessThan1.size() % 2 == 1) {
		result += lessThan1.back();
		lessThan1.pop_back();
	}

	for (int i = 1; i < greaterThan1.size(); i += 2) {
		result += greaterThan1[i] * greaterThan1[i - 1];
	}
	for (int i = 1; i < lessThan1.size(); i += 2) {
		result += lessThan1[i] * lessThan1[i - 1];
	}
	cout << result;
}

int main() {
	solve();
	return 0;
}
