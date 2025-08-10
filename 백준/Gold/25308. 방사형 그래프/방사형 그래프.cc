#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
using vector2d = pair<double, double>;

const double quarterPi = acos(-1) / 4;
vector<int> a(8);
vector<vector2d> permutation(9);
vector<bool> used(8, false);
int result = 0;

double det(vector2d a, vector2d b) {
	return a.first * b.second - b.first * a.second;
}

vector2d dist(vector2d from, vector2d to) {
	return make_pair(to.first - from.first, to.second - from.second);
}

void check() {
	permutation[8] = permutation[0];
	vector2d prev = dist(permutation[7], permutation[8]), now;
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
		permutation[i] = make_pair(a[x] * sin(quarterPi * i), a[x] * cos(quarterPi * i));
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
