#include <iostream>
#include <unordered_set>
#include <cmath>

using namespace std;

struct PointHash {
  size_t operator()(const pair<int, int>& p) const {
	return (static_cast<long long>(p.first) << 32) ^ (unsigned)p.second;
  }
};

int solve() {
  int n;
  cin >> n;
  unordered_set<pair<int, int>, PointHash> s;
  for (int i = 0; i < n; ++i) {
	int x, y;
	cin >> x >> y;
	s.emplace(x, y);
  }
  int result = 0;
  auto ed = s.end();
  for (auto A = s.begin(); A != ed; ++A) {
	auto B = A;
	while (++B != ed) {
	  int x = B->first - A->first;
	  int y = B->second - A->second;
	  if ((s.find(make_pair(A->first + y, A->second - x)) != ed
		&& s.find(make_pair(B->first + y, B->second - x)) != ed)
		|| (s.find(make_pair(A->first - y, A->second + x)) != ed
		&& s.find(make_pair(B->first - y, B->second + x)) != ed)) {
		result = max(result, x * x + y * y);
	  }
	}
  }
  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  int t;
  cin >> t;
  while (t--)
	cout << solve() << '\n';
  return 0;
}
