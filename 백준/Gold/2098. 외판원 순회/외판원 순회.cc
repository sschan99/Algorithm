#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int n;
vector<vector<int>> matrix;
const int inf = 1e9;

int dfs(vector<vector<int>>& dp, int visited, int last) {
  if (visited == (1 << n) - 1) {
	dp[visited][last] = matrix[last][0] == 0 ? inf : matrix[last][0];
  }
  else if (dp[visited][last] == 0) {
	int temp = inf;
	for (int i = 1; i < n; i++) {
	  if (visited & (1 << i) || matrix[last][i] == 0) {
		continue;
	  }
	  temp = min(temp, matrix[last][i] + dfs(dp, visited | (1 << i), i));
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

  cout << dfs(dp, 1, 0);

  return 0;
}
