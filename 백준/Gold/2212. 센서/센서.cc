#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

static int solve() {
	int N, K;
	cin >> N >> K;

	vector<int> v(N);
	for (int& i : v) cin >> i;
	sort(v.begin(), v.end());

	if (N < K) return 0;

	vector<int> diff(N - 1);
	for (size_t i = 0; i + 1 < N; i++) {
		diff[i] = v[i + 1] - v[i];
	}
	sort(diff.begin(), diff.end());

	return accumulate(diff.begin(), diff.end() - K + 1, 0);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cout << solve();
	return 0;
}
