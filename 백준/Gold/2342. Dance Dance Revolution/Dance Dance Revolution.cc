#include <iostream>
#include <vector>
using namespace std;

static int cost(int from, int to) {
  if (from == to)
	return 1;
  if (from == 0)
	return 2;
  if (abs(from - to) == 2)
	return 4;
  return 3;
}

int main() {
  const int inf = 1000000;

  vector<vector<int>> dp(5, vector<int>(5, inf));
  dp[0][0] = 0;

  int x;
  cin >> x;
  while (x != 0) {
	vector<vector<int>> next(5, vector<int>(5, inf));

	for (int l = 0; l < 5; l++) {
	  for (int r = 0; r < 5; r++) {
		if (r != x) {
		  next[x][r] = min(next[x][r], dp[l][r] + cost(l, x));
		}
		if (l != x) {
		  next[l][x] = min(next[l][x], dp[l][r] + cost(r, x));
		}
	  }
	}
	
	dp.swap(next);
	cin >> x;
  }

  int result = inf;
  for (auto row : dp) {
	for (auto elem : row) {
	  result = min(result, elem);
	}
  }
  cout << result;

  return 0;
}
