#include <iostream>
#include <vector>

using namespace std;

bool in(int x, int y, int cx, int cy, int r) {
  return (x - cx) * (x - cx) + (y - cy) * (y - cy) < r * r;
}

int solve() {
  int x1, y1, x2, y2;
  cin >> x1 >> y1 >> x2 >> y2;
  int n;
  cin >> n;
  int count = 0;
  for (int i = 0; i < n; ++i) {
	int cx, cy, r;
	cin >> cx >> cy >> r;
	if (in(x1, y1, cx, cy, r) != in(x2, y2, cx, cy, r))
	  ++count;
  }
  return count;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  while (T--) {
	cout << solve() << '\n';
  }
  return 0;
}
