#include <iostream>
#include <cmath>

using namespace std;

int solve() {
	int x1, y1, r1, x2, y2, r2;
	cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

	if (x1 == x2 && y1 == y2)
		return r1 == r2 ? -1 : 0;

	int dx = x2 - x1, dy = y2 - y1;
	double dist = sqrt(dx * dx + dy * dy);
	
	if (r1 < r2) swap(r1, r2);

	if (r1 + r2 < dist || r1 - r2 > dist) return 0;
	if (r1 + r2 > dist && dist > r1 - r2) return 2;
	return 1;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	while (T--)
		cout << solve() << '\n';
	return 0;
}
