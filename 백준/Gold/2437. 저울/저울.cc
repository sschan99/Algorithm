#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static int solve() {
	int N;
	cin >> N;
	vector<int> v(N);
	for (int& x : v) cin >> x;
	sort(v.begin(), v.end());

	int result = 1;
	for (int x : v) {
		if (result < x) break;
		result += x;
	}
    return result;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cout << solve();
	return 0;
}
