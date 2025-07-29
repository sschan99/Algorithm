#include <iostream>
#include <cmath>

using namespace std;

static void solve() {
	double x, y, c;
	cin >> x >> y >> c;

	double xSquare = x * x, ySquare = y * y;

	double low = 0, high = min(x, y);
	double h1, h2, w = high / 2;

	while (low + 0.001 < high) {
		h1 = sqrt(xSquare - w * w);
		h2 = sqrt(ySquare - w * w);

		if (c > h1 * h2 / (h1 + h2)) high = w;
		else low = w;
		w = (low + high) / 2;
	}
	cout << w;
}

int main() {
	solve();
	return 0;
}
