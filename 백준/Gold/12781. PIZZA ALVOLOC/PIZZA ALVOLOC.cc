#include <iostream>
#include <vector>

using namespace std;

static long det(int a, int b, int c, int d) {
	return 1l * a * d - 1l * b * c;
}

static int check(pair<int, int> a, pair<int, int> b) {
	long result = det(a.first, a.second, b.first, b.second);
	if (result > 0) return 1;
	if (result < 0) return -1;
	return 0;
}

static pair<int, int> dist(pair<int, int> from, pair<int, int> to) {
	return make_pair(to.first - from.first, to.second - from.second);
}

static bool solve() {
	vector<pair<int, int>> v(4);
	for (auto& p : v) cin >> p.first >> p.second;

	pair<int, int> to1, to2, to3;
	to1 = dist(v[0], v[1]);
	to2 = dist(v[0], v[2]);
	to3 = dist(v[0], v[3]);

	int result1 = check(to1, to2);
	int result2 = check(to1, to3);
	if (result1 == 0 || result2 == 0) return false;
	return result1 * result2 != 0 && result1 != result2;
}

int main() {
	cout << solve();
	return 0;
}
