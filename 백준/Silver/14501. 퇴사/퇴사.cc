#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<pair<int, int>> v(n);
  for (auto& [t, p] : v) cin >> t >> p;

  vector<int> dp(n + 1, 0);

  for (int i = n - 1; i >= 0; i--) {
	auto& [t, p] = v[i];
	if (i + t > n) {
	  dp[i] = dp[i + 1];
	}
	else {
	  dp[i] = max(dp[i + t] + p, dp[i + 1]);
	}
  }
  cout << dp[0];
  return 0;
}
