#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static void solve() {
	int N, S, T;
	cin >> N;

	vector<pair<int, int>> data;
	data.reserve(N * 2);

	while (N--) {
		cin >> S >> T;
		data.push_back(make_pair(S, 1));
		data.push_back(make_pair(T, -1));
	}
	sort(data.begin(), data.end());

	int maximum = 0, now = 0;
	for (auto& p : data) {
		now += p.second;
		if (maximum < now) maximum = now;
	}
	cout << maximum;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	solve();
	return 0;
}
