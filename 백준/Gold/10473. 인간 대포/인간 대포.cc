#include <iostream>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

struct Point {
  double x, y;
  double dist(Point other) {
	return sqrt((other.x - x) * (other.x - x) + (other.y - y) * (other.y - y));
  }
};

double solve() {
  Point A, B;
  cin >> A.x >> A.y >> B.x >> B.y;
  int n;
  cin >> n;
  vector<Point> cannon(n);
  for (Point& p : cannon) cin >> p.x >> p.y;
  
  vector<double> time(n, -1);
  priority_queue<pair<double, int>> pq;
  for (int i = 0; i < n; ++i)
	pq.emplace(-(A.dist(cannon[i]) / 5.0), i);

  while (!pq.empty()) {
	pair<double, int> p = pq.top();
	pq.pop();
	double t = -p.first;
	int i = p.second;
	if (time[i] != -1) continue;
	time[i] = t;
	for (int j = 0; j < n; ++j) {
	  double d = cannon[i].dist(cannon[j]);
	  pq.emplace(-(t + d / 5.0), j);
	  pq.emplace(-(t + 2.0 + abs(d - 50.0) / 5.0), j);
	}
  }
  double result = A.dist(B) / 5.0;
  for (int i = 0; i < n; ++i) {
	double d = cannon[i].dist(B);
	double t = time[i] + min(d / 5.0, 2.0 + abs(d - 50.0) / 5.0);
	result = min(result, t);
  }
  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout.precision(6);
  cout << fixed << solve();
  return 0;
}
