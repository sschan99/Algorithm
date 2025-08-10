#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Point {
	double x, y;
};

const double quarterPi = acos(-1) / 4;
vector<int> a(8);
vector<Point> permutation(9);
vector<bool> used(8, false);
int result = 0;

double det(Point a, Point b) {
	return a.x * b.y - b.x * a.y;
}

Point dist(Point from, Point to) {
	Point p;
	p.x = to.x - from.x;
	p.y = to.y - from.y;
	return p;
}

void check() {
	permutation[8] = permutation[0];
	Point prev = dist(permutation[7], permutation[8]), now;
	for (size_t i = 0; i < 8; i++) {
		now = dist(permutation[i], permutation[i + 1]);
		if (det(prev, now) > 0) {
			return;
		}
		prev = now;
	}
	result++;
}

void recursion(int i) {
	if (i == 8) {
		return check();
	}
	for (int x = 0; x < 8; x++) {
		if (used[x]) continue;
		Point p;
		p.x = a[x] * sin(quarterPi * i);
		p.y = a[x] * cos(quarterPi * i);
		permutation[i] = p;
		used[x] = true;
		recursion(i + 1);
		used[x] = false;
	}
}

int main() {
	for (int& i : a) cin >> i;
	recursion(0);
	cout << result;
	return 0;
}
