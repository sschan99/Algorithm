#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int n;
vector<vector<int>> matrix;
const int inf = 1e9;

int dfs(vector<vector<int>>& dp, int visited, int last) {
  if (dp[visited][last] == 0) {
	int prev = visited ^ (1 << last);
	int temp = inf;
	for (int i = 0; i < n; i++) {
	  if ((prev & (1 << i)) && matrix[i][last] != 0) {
		temp = min(temp, dfs(dp, prev, i) + matrix[i][last]);
	  }
	}
	dp[visited][last] = temp;
  }
  return dp[visited][last];
}

int main() {
  cin >> n;

  matrix.resize(n);
  for (auto& row : matrix) {
	row.resize(n);
	for (int& elem : row) {
	  cin >> elem;
	}
  }
  vector<vector<int>> dp(1 << n, vector<int>(n, 0));
  for (int i = 0; i < n; i++) {
	dp[1 << i][i] = matrix[0][i] == 0 ? inf : matrix[0][i];
  }
  cout << dfs(dp, (1 << n) - 1, 0);

  return 0;
}
