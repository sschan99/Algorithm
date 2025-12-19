#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> v(n);
  for (int& x : v) cin >> x;

  vector<int> dp = v;

  for (int i = 1; i < n; i++) {
	dp[i] = max(dp[i], dp[i - 1] + v[i]);
  }
  cout << *max_element(dp.begin(), dp.end());

  return 0;
}
