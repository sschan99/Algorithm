#include <iostream>

using namespace std;

void solve() {
	int x1, y1, x2, y2, x3, y3, x, y;
	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

	x = x1 == x2 ? x3 : x1 == x3 ? x2 : x1;
	y = y1 == y2 ? y3 : y1 == y3 ? y2 : y1;

	cout << x << ' ' << y << '\n';
}

int main() {
	solve();
	return 0;
}
