#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int n, m, k;
  cin >> n >> m >> k;

  vector<int> candy(n);
  for (int& x : candy) cin >> x;

  vector<vector<int>> edge(n + 1);
  for (int i = 0; i < m; i++) {
	int a, b;
	cin >> a >> b;
	edge[a].push_back(b);
	edge[b].push_back(a);
  }

  vector<bool> visited(n + 1, false);
  queue<int> q;
  vector<int> cost, value;

  for (int i = 1; i <= n; i++) {
	if (visited[i])
	  continue;
	visited[i] = true;
	q.push(i);
	cost.push_back(1);
	value.push_back(candy[i - 1]);

	while (!q.empty()) {
	  int u = q.front();
	  q.pop();

	  for (int& v : edge[u]) {
		if (visited[v])
		  continue;
		visited[v] = true;
		q.push(v);
		cost.back() += 1;
		value.back() += candy[v - 1];
	  }
	}
  }

  int x = cost.size();
  vector<int> dp(k, 0);

  for (int i = 0; i < x; i++) {
	int c = cost[i], v = value[i];

	for (int j = k - 1; j >= c; j--) {
	  dp[j] = max(dp[j - c] + v, dp[j]);
	}
  }
  cout << dp.back();

  return 0;
}
