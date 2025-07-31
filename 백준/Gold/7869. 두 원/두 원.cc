#include <iostream>
#include <cmath>

using namespace std;

static double solve() {
	double x1, y1, r1, x2, y2, r2;
	cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
	double dx = x2 - x1, dy = y2 - y1;
	double d = sqrt(dx * dx + dy * dy);

	if (d > r1 + r2) return 0.;
	if (d + r1 <= r2) return r1 * r1 * acos(-1);
	if (d + r2 <= r1) return r2 * r2 * acos(-1);

	double theta1 = acos((r1 * r1 + d * d - r2 * r2) / (2 * r1 * d)) * 2;
	double theta2 = acos((r2 * r2 + d * d - r1 * r1) / (2 * r2 * d)) * 2;
	double s1 = r1 * r1 * sin(theta1) / 2;
	double s2 = r2 * r2 * sin(theta2) / 2;
	return (r1 * r1 * theta1 + r2 * r2 * theta2) / 2 - s1 - s2;
}

int main() {
	printf("%.3f", solve());
	return 0;
}
