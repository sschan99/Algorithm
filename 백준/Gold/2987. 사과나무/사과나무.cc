#include <iostream>
#include <cmath>

using namespace std;

long det(int a, int b, int c, int d) {
  return 1l * a * d - 1l * b * c;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int ax, ay, bx, by, cx, cy;
  cin >> ax >> ay >> bx >> by >> cx >> cy;

  int t, x, y, count = 0;
  cin >> t;
  while (t--) {
	cin >> x >> y;
	long dab = det(bx - ax, by - ay, x - ax, y - ay);
	long dbc = det(cx - bx, cy - by, x - bx, y - by);
	long dca = det(ax - cx, ay - cy, x - cx, y - cy);
	if ((dab >= 0 && dbc >= 0 && dca >= 0) || (dab <= 0 && dbc <= 0 && dca <= 0))
	  ++count;
  }

  double s = abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) / 2.0;
  cout.precision(1);
  cout << fixed << s << '\n';
  cout << count << '\n';

  return 0;
}
