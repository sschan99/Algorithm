#include <iostream>
#include <cmath>

using namespace std;

struct Point {
	double x, y;
	Point(double _x = 0, double _y = 0) : x(_x), y(_y) {}
};

double dist(const Point& p, const Point& q) {
	return sqrt((q.x - p.x) * (q.x - p.x) + (q.y - p.y) * (q.y - p.y));
}

double solve() {
	Point a, b, c, d;
	cin >> a.x >> a.y >> b.x >> b.y >> c.x >> c.y >> d.x >> d.y;

	double low = 0, high = 1, dist_i, dist_j;
	while (low + 0.0000000001 < high) {
		double i = low + (high - low) / 3;
		double j = high - (high - low) / 3;
		dist_i = dist(
			Point(a.x * (1 - i) + b.x * i, a.y * (1 - i) + b.y * i),
			Point(c.x * (1 - i) + d.x * i, c.y * (1 - i) + d.y * i)
		);
		dist_j = dist(
			Point(a.x * (1 - j) + b.x * j, a.y * (1 - j) + b.y * j),
			Point(c.x * (1 - j) + d.x * j, c.y * (1 - j) + d.y * j)
		);
		if (dist_i < dist_j) high = j;
		else low = i;
	}
	return min(dist_i, dist_j);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cout.precision(10);
	cout << fixed << solve();
	return 0;
}
