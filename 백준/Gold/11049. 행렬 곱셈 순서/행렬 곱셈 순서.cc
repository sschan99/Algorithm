#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<pair<int, int>> mat(n);
  for (auto& [r, c] : mat) {
	cin >> r >> c;
  }
  vector<vector<int>> dp(n, vector<int>(n, 0));

  for (int w = 1; w < n; w++) {
	for (int i = 0; i + w < n; i++) {
	  int k = i + w;
	  int min_value = INT_MAX;
	  for (int j = i; j < k; j++) {
		int temp = mat[i].first * mat[j].second * mat[k].second;
		min_value = min(min_value, dp[i][j] + dp[j + 1][k] + temp);
	  }
	  dp[i][k] = min_value;
	}
  }
  cout << dp[0][n - 1];

  return 0;
}