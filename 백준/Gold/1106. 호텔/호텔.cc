#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int solve() {
  int c, n, cost, value;
  cin >> c >> n;

  vector<int> dp(c + 1, INT_MAX);
  dp[0] = 0;
  
  for (int _ = 0; _ < n; ++_) {
	cin >> cost >> value;
	for (int i = 0; i <= c; ++i) {
	  dp[i] = min(dp[i], (i - value < 0) ? cost : dp[i - value] + cost);
	}
  }
  return dp[c];
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve();
  return 0;
}
