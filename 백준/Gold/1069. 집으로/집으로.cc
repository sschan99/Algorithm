#include <iostream>
#include <cmath>

using namespace std;

double solve() {
	int X, Y, D, T;
	cin >> X >> Y >> D >> T;

	double dist = sqrt(X * X + Y * Y);
	if (D < T) return dist;
	if (dist < D) return min(min(dist, T + D - dist), 2. * T);

	int q = (int)dist / D;
	double r = fmod(dist, D);
	
	return q * T + min(r, (double)T);
}

int main() {
	cout << fixed;
	cout.precision(9);
	cout << solve();
	return 0;
}
