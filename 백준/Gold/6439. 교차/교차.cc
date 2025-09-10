#include <iostream>

using namespace std;

struct Point {
  int x, y;
  Point(int x, int y) : x(x), y(y) {}
};

long det(int a, int b, int c, int d) {
  return a * d - b * c;
}

bool connect(Point a1, Point a2, Point b1, Point b2) {
  long d1, d2, d3, d4;
  d1 = det(a2.x - a1.x, a2.y - a1.y, b1.x - a1.x, b1.y - a1.y);
  d2 = det(a2.x - a1.x, a2.y - a1.y, b2.x - a1.x, b2.y - a1.y);
  if (d1 > d2) swap(d1, d2);
  if (d1 == 0 && d2 == 0) {
	return (b1.x - a1.x) * (b2.x - a1.x) + (b1.y - a1.y) * (b2.y - a1.y) <= 0
	  || (b1.x - a2.x) * (b2.x - a2.x) + (b1.y - a2.y) * (b2.y - a2.y) <= 0
	  || (a1.x - b1.x) * (a2.x - b1.x) + (a1.y - b1.y) * (a2.y - b1.y) <= 0
	  || (a1.x - b2.x) * (a2.x - b2.x) + (a1.y - b2.y) * (a2.y - b2.y) <= 0;
  }
  d3 = det(b2.x - b1.x, b2.y - b1.y, a1.x - b1.x, a1.y - b1.y);
  d4 = det(b2.x - b1.x, b2.y - b1.y, a2.x - b1.x, a2.y - b1.y);
  if (d3 > d4) swap(d3, d4);
  return !(d1 > 0 || d2 < 0 || d3 > 0 || d4 < 0);
}

bool solve() {
  int x_start, y_start, x_end, y_end, left, top, right, bottom;
  cin >> x_start >> y_start >> x_end >> y_end >> left >> top >> right >> bottom;
  if (left > right) swap(left, right);
  if (bottom > top) swap(bottom, top);
  Point start(x_start, y_start), end(x_end, y_end),
	lt(left, top), rt(right, top), lb(left, bottom), rb(right, bottom);
  return (x_start >= left && x_start <= right && y_start >= bottom && y_start <= top)
	|| (x_end >= left && x_end <= right && y_end >= bottom && y_end <= top)
	|| connect(start, end, lt, rt) || connect(start, end, lb, rb)
	|| connect(start, end, lb, lt) || connect(start, end, rb, rt);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;
  while (t--)
	cout << (solve() ? 'T' : 'F') << '\n';
  return 0;
}
