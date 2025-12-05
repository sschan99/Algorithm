#include <iostream>
#include <vector>
using namespace std;

const int d = 1e9;
const int range = 1 << 10;

int main() {
  int n;
  cin >> n;

  vector<vector<int>> dp(range, vector<int>(10, 0));
  for (int i = 1; i < 10; i++) {
	int mask = 1 << i;
	dp[mask][i] = 1;
  }

  while (--n) {
	vector<vector<int>> next(range, vector<int>(10, 0));
	for (int mask = 1; mask < range; mask++) {
	  for (int i = 0; i < 9; i++) {
		int& a = next[mask | (1 << (i + 1))][i + 1];
		a = (a + dp[mask][i]) % d;
	  }
	  for (int i = 1; i < 10; i++) {
		int& b = next[mask | (1 << (i - 1))][i - 1];
		b = (b + dp[mask][i]) % d;
	  }
	}
	dp.swap(next);
  }

  int result = 0;
  for (int x : dp[range - 1]) {
	result = (result + x) % d;
  }
  cout << result;

  return 0;
}
