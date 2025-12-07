#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<vector<int>> dp(30, vector<int>(30, 0));
  for (int j = 1; j < 30; j++) {
	dp[1][j] = j;
  }
  for (int i = 2; i < 30; i++) {
	for (int j = i; j < 30; j++) {
	  dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1];
	}
  }

  int t;
  cin >> t;
  while (t--) {
	int n, m;
	cin >> n >> m;
	cout << dp[n][m] << '\n';
  }

  return 0;
}