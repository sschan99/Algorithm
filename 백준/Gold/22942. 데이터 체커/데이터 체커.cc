#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool solve() {
  int n, x, r;
  cin >> n;
  vector<pair<int, int>> v(n), stack;
  for (auto& p : v) {
	cin >> x >> r;
	p.first = x - r;
	p.second = x + r;
  }
  sort(v.begin(), v.end());
  for (auto& p : v) {
	while (!stack.empty() && stack.back().second < p.first) {
	  stack.pop_back();
	}
	if (stack.empty() || (stack.back().first < p.first && p.second < stack.back().second)) {
	  stack.push_back(p);
	  continue;
	}
	return false;
  }
  return true;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << (solve() ? "YES" : "NO");
  return 0;
}
