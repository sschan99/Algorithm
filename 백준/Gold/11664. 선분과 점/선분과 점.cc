#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct vector3d {
  double i, j, k;

  vector3d(double i = 0, double j = 0, double k = 0) : i(i), j(j), k(k) {}

  double magnitude() const {
	return sqrt(i * i + j * j + k * k);
  }
  
  vector3d operator+(const vector3d& other) const {
	return vector3d(i + other.i, j + other.j, k + other.k);
  }

  vector3d operator-(const vector3d& other) const {
	return vector3d(i - other.i, j - other.j, k - other.k);
  }

  vector3d operator*(double d) const {
	return vector3d(i * d, j * d, k * d);
  }
};

double solve() {
  vector3d A, B, C;
  cin >> A.i >> A.j >> A.k >> B.i >> B.j >> B.k >> C.i >> C.j >> C.k;

  double low = 0, high = 1;
  double p, q, pValue, qValue;

  while (low + 1e-15 < high) {
	p = (2 * low + high) / 3;
	q = (low + 2 * high) / 3;

	pValue = (C - (A * (1 - p) + B * p)).magnitude();
	qValue = (C - (A * (1 - q) + B * q)).magnitude();
	
	if (pValue < qValue) {
	  high = q;
	} else {
	  low = p;
	}
  }
  return pValue;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout.precision(10);
  cout << fixed << solve() << '\n';
  return 0;
}
