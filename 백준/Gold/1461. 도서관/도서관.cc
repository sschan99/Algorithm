#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve() {
  int n, m, x;
  cin >> n >> m;
  vector<int> left, right;
  for (int i = 0; i < n; ++i) {
	cin >> x;
	if (x < 0) {
	  left.push_back(-x);
	} else {
	  right.push_back(x);
	}
  }
  sort(left.rbegin(), left.rend());
  sort(right.rbegin(), right.rend());
  
  int result = 0;
  for (int i = 0; i < left.size(); i += m) {
	result += left[i] * 2;
  }
  for (int i = 0; i < right.size(); i += m) {
	result += right[i] * 2;
  }
  return result - max(left.empty() ? 0 : left[0], right.empty() ? 0 : right[0]);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve() << '\n';
  return 0;
}
