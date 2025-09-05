#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solve() {
  int n;
  cin >> n;
  vector<int> rope(n);
  for (int& i : rope) cin >> i;
  sort(rope.rbegin(), rope.rend());

  int result = 0;

  for (int i = 0; i < n; ++i) {
	int x = (i + 1) * rope[i];
	result = max(result, x);
  }
  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve();
  return 0;
}
