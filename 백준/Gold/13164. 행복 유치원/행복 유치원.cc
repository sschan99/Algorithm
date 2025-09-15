#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve() {
  int n, k, prev, now;
  cin >> n >> k >> prev;
  vector<int> diff(n - 1);
  for (int i = 0; i < n - 1; ++i) {
	cin >> now;
	diff[i] = now - prev;
	prev = now;
  }
  sort(diff.begin(), diff.end());
  long result = 0, i = 0;
  while (i < n - k) {
	result += diff[i++];
  }
  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  cout << solve() << '\n';
  return 0;
}
