#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <climits>

using namespace std;

int solve() {
  int n, k, x;
  cin >> n >> k;
  
  vector<int> dp(k + 1, INT_MAX - 1);
  dp[0] = 0;
  for (int i = 0; i < n; i++) {
	cin >> x;
	for (int j = x; j < k + 1; j++) {
	  dp[j] = min(dp[j], dp[j - x] + 1);
	}
  }
  return (dp[k] == INT_MAX - 1) ? -1 : dp[k];
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve() << '\n';
  return 0;
}