#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int xa, ya, xb, yb, xc, yc;
  cin >> xa >> ya >> xb >> yb >> xc >> yc;

  int a, b, c, d, e, f;
  a = xb - xa;
  b = yb - ya;
  c = xc - xa;
  d = yc - ya;
  e = xb - xc;
  f = yb - yc;

  if (a * d == b * c) {
	cout << -1;
	return 0;
  }

  double v1, v2, v3;
  v1 = sqrt(a * a + b * b);
  v2 = sqrt(c * c + d * d);
  v3 = sqrt(e * e + f * f);

  if (v1 > v2) swap(v1, v2);
  if (v2 > v3) swap(v2, v3);
  if (v1 > v2) swap(v1, v2);

  cout.precision(16);
  cout << fixed << (v3 * 2 - v1 * 2);

  return 0;
}
