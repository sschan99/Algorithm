#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solve() {
  int n;
  cin >> n;
  vector<pair<int, int>> v(n);
  for (auto& p : v)
	cin >> p.second >> p.first;
  sort(v.begin(), v.end());
  if (n == 0) return 0;
  int t = v.back().first;
  priority_queue<int> pq;
  int result = 0;
  while (t > 0) {
	while (!v.empty() && v.back().first >= t) {
	  pq.push(v.back().second);
	  v.pop_back();
	}
	if (!pq.empty()) {
	  result += pq.top();
	  pq.pop();
	}
	--t;
  }
  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve() << '\n';
  return 0;
}
